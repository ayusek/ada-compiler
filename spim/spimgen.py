#!/usr/bin/env python

#Spim Code generation was seen from https://www.cs.tcd.ie/~waldroj/itral/spim_ref.html

from three_addrcode_functions import * #Has symbol Table in it
code = []

#we have the current register context with us
def getreg(variable , selector): #0 for operand 1 , 1 for operand 2, 2 for result
	regname = 't' + str(selector)
	return regname

def loadintoreg(variable , selector = 0):
	if isinstance(selector , str):
		reg = selector

	else:
		if(selector == 2):
			return getreg(variable , selector)

		if(selector == -1):
			reg = "a0"

		else:		
			reg = getreg(variable , selector)

	if isinstance(variable,int):
		code.append('\tli $' + reg + ', ' + str(variable))

	elif isinstance(variable , float):
		code.append('\tli.s $' + reg + ', ' + str(variable))


	elif '\'' in variable: #character
		code.append('\tli $' + reg + ', ' + variable)

	elif '(' in variable:
		variable = variable.split('(')[0]
		offset_variable  = (variable.split('(')[1]).split(')')[0]
		temp_reg = getreg(offset_variable , 3)
		code.append('\tli $'+ reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')))
		code.append('\tadd $' + reg + ', $sp, $' + reg)
		code.append('\tlw $' + temp_reg +  ", " + str(symbol_table.get_Attribute_Value(offset_variable , 'offset')) + "($sp)")
		code.append('\tadd $' + temp_reg + ', $'+ temp_reg +', $' + reg)
		code.append('\tlw $' + reg + ', ($' + temp_reg +')')

	elif isinstance(variable , str) :	
		code.append('\tlw $'+ reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')) + '($sp)')

	else :
		print "Unknow type of argument passed " + variable
		reg = None

	return reg #reg not contains its value

def regtoMem(reg , variable):
	if '(' in variable: #array support
		variable = variable.split('(')[0]
		offset_variable  = (variable.split('(')[1]).split(')')[0]
		temp_reg = getreg(offset_variable , 3)
		temp_reg1 = getreg(offset_variable , 4)
		code.append('\tli $'+ temp_reg1 + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')))
		code.append('\tadd $' + temp_reg1+ ', $sp, $' + temp_reg1)
		code.append('\tlw $' + temp_reg +  ", " + str(symbol_table.get_Attribute_Value(offset_variable , 'offset')) + "($sp)")
		code.append('\tadd $' + temp_reg + ', $'+ temp_reg +', $' + temp_reg1)
		code.append('\tsw $' + reg + ', ($' + temp_reg + ')')

	else:
		code.append('\tsw $' + reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')) + '($sp)')

#Returns a string of instructions
def TAC2spim( three_addr_code , main_procedure_name):

	global symbol_table
	global code

	target_count = 0 
	parameter_count = 0 
	out_parameter_count = 0 

	if not symbol_table.locate_Symbol_in_this(main_procedure_name):
		print "[Error] : File name must match the global function name"
		return ''

	#					DATA Segment

	symbol_table.set_current_table(symbol_table.get_Attribute_Value(main_procedure_name , 'SymbolTable'))

	code.append(".data") 
	code.append('\tnewline : .asciiz "\\n"')

	'''
	#creating all the  main procedure variables 
	for item in symbol_table.get_Hash_Table():
		if(symbol_table.get_Attribute_Value(item , "SymbolTable") != None):
			#This is a procedure
			continue

		if( not (symbol_table.get_Attribute_Value(item , "istype") == True) ):
			width = symbol_table.get_Attribute_Value(item, "width")
			if(int(width)%4 == 0):
				code.append('\t' + item + " : .space " + str(width))
			else:
				code.append('\t' + item + " : .align " + str(width))

	'''
	#============Add more stuff related to data segment here

	#Starting the implementation
	code += ['\n.text' , 'main:' , '\tjal ProcLabel_' + main_procedure_name , '\tla $sp, 0($sp)' , '\tj exit']
	
	no_params = 0

 	for instr in three_addr_code.get_list() :
 		code.append('L' + str(instr[0]) + ":")

 		operator = instr[3]
 		result = instr[1]
 		operand1 = instr[2]
 		operand2 = instr[4]

 		if operator in ['int_+','int_-' , 'int_*' , 'int_/' , '+' , '-' , '*' , '/']:
 			reg_result = loadintoreg(result , 2) #Does not loads anything
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)	
 			if operator in ['int_+', '+']:
 				code.append('\tadd $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['int_-', '-']:
 				code.append('\tsub $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['int_*', '*']:
 				code.append('\tmul $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['int_/', '/']:
 				code.append('\tdiv $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 		
 			regtoMem( reg_result , result)

 		if operator == ":=":
 			reg = loadintoreg(operand1)
 			regtoMem(reg , result)
 			#Received three registers

 		if operator == "int_un+" or operator == "float_un+":
 			reg_operand2 = loadintoreg(operand2)
  			regtoMem(reg_operand2 , result)

 		if operator == "int_un-" or operator == "float_un-":
 			reg_result = loadintoreg(result , 2)
 			reg_operand2 = loadintoreg(operand2)
 			code.append('\tneg $' + reg_operand2 +', $' + reg_result)
 			regtoMem(reg_result , result)

 		if operator == "syscall":
 			if result == "Print_int":
 				code.append('\tli $v0'  + ', ' + '1')
 				reg = loadintoreg(operand1  , -1)
 				code.append('\tsyscall')


 			elif result == "Print_float":
 				code.append('\tli $v0'  + ', ' + '2')
 				reg = loadintoreg(operand1 , -1)
  				code.append('\tsyscall')


 			elif result == "Print_char":
 				code.append('\tli $v0'  + ', ' + '11')
 				reg = loadintoreg(operand1 , -1)
  				code.append('\tsyscall')


 			elif result == "Print_newline":
 				code.append('\tli $v0'  + ', ' + '4')
 				code.append('\tla $a0'  + ', ' + 'newline')
   				code.append('\tsyscall')

 			else:
 				print "Syscall " + result + " not found" 

 		#Handling Procedures
 		if operator  == "proc_label":
 			code.append("ProcLabel_" + result + ":")

 			width = symbol_table.get_Attribute_Value(result , "width")
 			#Currently in the symbol table of the senior
 			symbol_table.set_current_table(symbol_table.get_Attribute_Value(result , "SymbolTable"))
 			#Keeping a space of 32 for other data
 			#Data is stores in a reverse format
 			code += [ '\tsw $fp, -4($sp)' , '\tsw $ra, -8($sp)' , '\tla $fp, 0($sp)' , '\tla $sp, -' + str(32 + width) + '($sp)']

 			reg = "a0"

 			count = 0 
 			#Copying the values to the space of these variable


 		if operator == "return" :
 			#operand1 stores the variable list
 			if (operand1 != None):
 				returnvars = operand1.split(' ')[1:]
 				#the computed values are returned in $vi

 				for i in range(0,len(returnvars)):
 					loadintoreg(returnvars[i] , "v" + str(i) )  #Returned in the order or the return
 				
 				out_count_variables = len(returnvars) - 1


 			symbol_table.set_current_table(symbol_table.get_current_table().prev_table)
 			code += ['\tla $sp, 0($fp)', '\tlw $ra, -8($fp)', '\tlw $fp, -4($sp)' , '\tjr $ra']

 		if operator == "PullParam" :
 			#Restoring the symbol table
 			regtoMem("v" + str(out_count_variables) , result) #storing the information in the return parameters to their corresponding addresses
 			out_count_variables -= 1
 		
 		if operator == "procedure_call":
 			parameter_count = len(operand2)
 			out_count_variables = len(operand2) - parameter_count
 			width = symbol_table.get_Attribute_Value(operand1 , "width") + 32
 			#sp is going to go down by this measure
 			count = 0 
 			for item in operand2:
 				reg =  loadintoreg(item , 0)
 				code.append('\tsw $' + reg + ', ' + str(count*4 - width) + '($sp)')
 				count += 1

 			code.append('\tjal ProcLabel_' + operand1)
 		
 		if operator == "makelabel":
 			code.append(result + ":")

 		if operator == "=" :
 			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tseq $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)

 		if operator == "/=" :
 			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tsne $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)

 		if operator == "<" :
 			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tslt $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)

 		if operator == "<=" :
 			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tsle $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)
 
 		if operator == ">" :
 			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tsgt $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)

 		if operator == ">=" :
 			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tsge $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)

 		if operator == "goto":
 			if operand1 == None:
	 			if isinstance(result , int):
	 				code.append('\tj ' + 'L' + str(result))

	 			else:
	 				code.append('\tj ' + result)
	 		else:
	 			reg_operand1 = loadintoreg(operand1 , 1)

	 			if isinstance(result , int):
	 				code.append('\tbeq $' + reg_operand1 + ', 1, L' + str(result))

	 			else:
	 				code.append('\tbeq $' + reg_operand1 + ', 1, ' + result)



 		if operator == "blteq":
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

	 		if isinstance(result , int):
 				code.append('\tble $' + reg_operand1 + ', $' + reg_operand2+ ', L' + str(result))
	 		else:
	 			code.append('\tble $' + reg_operand1 + ', $' + reg_operand2+ ', ' + result)



 		if operator == "bgteq":
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

	 		if isinstance(result , int):
 				code.append('\tbge $' + reg_operand1 + ', $' + reg_operand2+ ', L' + str(result))
	 		else:
	 			code.append('\tbge $' + reg_operand1 + ', $' + reg_operand2+ ', ' + result)

	 	if operator == "and" :
	 		reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tand $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)

	 	if operator == "or" :
 			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1)

 			code.append('\tor $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result)

 		if operator == "starstar" :
			reg_result = loadintoreg(result , 2)
 			reg_operand1 = loadintoreg(operand1 , 0)
 			reg_operand2 = loadintoreg(operand2 , 1) 	

 			code.append('\tli $' + reg_result + ', 1')
 			code.append('start' + str(target_count) + ":")
 			code.append('\tble $' + reg_operand2 + ', 0, ' + "target" + str(target_count))
 			code.append('\tmul $' + reg_result + ', $' + reg_result + ', $' + reg_operand1)
 			code.append('\tsub $' + reg_operand2 + ', $' + reg_operand2 + ', 1')
 			code.append('\tj start' + str(target_count))
 			code.append("target" + str(target_count) + ":")
 			target_count += 1

 			regtoMem(reg_result , result)




 	for instr in three_addr_code.get_list():
 		print instr

 	code += ['\nexit:' , '\tli $v0, 10' , '\tsyscall']
 	return code
