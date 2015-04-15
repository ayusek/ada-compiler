#!/usr/bin/env python

#Spim Code generation was seen from https://www.cs.tcd.ie/~waldroj/itral/spim_ref.html

from three_addrcode_functions import * #Has symbol Table in it
code = []

#we have the current register context with us
def getreg(variable , selector , type): #0 for operand 1 , 1 for operand 2, 2 for result
	if (type == "float"):
		regname = 'f' + str(selector)
	else:
		regname = 't' + str(selector)
	return regname

def loadintoreg(variable , selector  , type):
	if isinstance(selector , str):
		reg = selector

	else:
		if(selector == 2):
			return getreg(variable , selector , type)

		if(selector == -1):
			if (type == "float"):
				reg = "f12"
			else:
				reg = "a0"

		else:		
			reg = getreg(variable , selector , type)

	if isinstance(variable,int):
		code.append('\tli $' + reg + ', ' + str(variable))

	elif isinstance(variable , float):
		code.append('\tli.s $' + reg + ', ' + str(variable))


	elif '\'' in variable: #character
		code.append('\tli $' + reg + ', ' + variable)

	elif '(' in variable:
		offset_variable  = (variable.split('(')[1]).split(')')[0]
		variable = variable.split('(')[0]

		temp_reg = getreg(offset_variable , 4 , "int")
		temp_reg2 = getreg(variable , 5 , "int")


		code.append('\tli $'+ temp_reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')))
		code.append('\tadd $' + temp_reg + ', $sp, $' + temp_reg)
		code.append('\tlw $' + temp_reg2 +  ", " + str(symbol_table.get_Attribute_Value(offset_variable , 'offset')) + "($sp)")
		code.append('\tadd $' + temp_reg + ', $'+ temp_reg +', $' + temp_reg2)

		if (type == "float"):
			code.append('\tl.s $' + reg + ', ($' + temp_reg +')')
		else:
			code.append('\tlw $' + reg + ', ($' + temp_reg +')')

	elif isinstance(variable , str) :	
		if (type == "float"):
			code.append('\tl.s $'+ reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')) + '($sp)')
		else:
			code.append('\tlw $'+ reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')) + '($sp)')

	else :
		print "Unknow type of argument passed " + variable
		reg = None

	return reg #reg not contains its value

def regtoMem(reg , variable , type):
	if '(' in variable: #array support
		offset_variable  = (variable.split('(')[1]).split(')')[0]
		variable = variable.split('(')[0]
		temp_reg = getreg(offset_variable , 3 , "int")
		temp_reg1 = getreg(offset_variable , 4 , "int")
		code.append('\tli $'+ temp_reg1 + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')))
		code.append('\tadd $' + temp_reg1+ ', $sp, $' + temp_reg1)
		code.append('\tlw $' + temp_reg +  ", " + str(symbol_table.get_Attribute_Value(offset_variable , 'offset')) + "($sp)")
		code.append('\tadd $' + temp_reg + ', $'+ temp_reg +', $' + temp_reg1)
		if (type == "float"):
			code.append('\ts.s $' + reg + ', ($' + temp_reg + ')')
		else:
			code.append('\tsw $' + reg + ', ($' + temp_reg + ')')

	else:
		if(type == "float"):
			code.append('\ts.s $' + reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')) + '($sp)')
		else:
			code.append('\tsw $' + reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')) + '($sp)')

#Returns a string of instructions
def TAC2spim( three_addr_code , main_procedure_name):

	global symbol_table
	global code

	target_count = 0 
	parameter_count = 0 
	out_parameter_count = 0
	float_count = 0
	newline_count = 0   

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

#ALgebra Expression
 		if operator in ['int_+','int_-' , 'int_*' , 'int_/' , '+' , '-' , '*' , '/']:
 			reg_result = loadintoreg(result , 2 , "int")  #Does not loads anything
 			reg_operand1 = loadintoreg(operand1 , 0 , "int")
 			reg_operand2 = loadintoreg(operand2 , 1 , "int")	
 			if operator in ['int_+', '+']:
 				code.append('\tadd $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['int_-', '-']:
 				code.append('\tsub $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['int_*', '*']:
 				code.append('\tmul $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['int_/', '/']:
 				code.append('\tdiv $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 		
 			regtoMem( reg_result , result , "int")

 		if operator in ['float_+','float_-' , 'float_*' , 'float_/']:
 			reg_result = loadintoreg(result , 2 , "float")  #Does not loads anything
 			reg_operand1 = loadintoreg(operand1 , 0 , "float")
 			reg_operand2 = loadintoreg(operand2 , 1 , "float")	

 			if operator in ['float_+']:
 				code.append('\tadd.s $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['float_-']:
 				code.append('\tsub.s $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['float_*']:
 				code.append('\tmul.s $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 			if operator in ['float_/']:
 				code.append('\tdiv.s $' + reg_result +', $' + reg_operand1 + ', $' + reg_operand2)
 		
 			regtoMem( reg_result , result , "float")

#Assignemnts
 		if operator == "int_:=":
 			reg = loadintoreg(operand1 , 0 , "int")
 			regtoMem(reg , result , "int")

 		if operator == "float_:=":
 			reg = loadintoreg(operand1 , 0 , "float")
 			regtoMem(reg , result , "float")
 			#Received three registers

#Unary Operators
 		if operator == "int_un+":
 			reg_operand2 = loadintoreg(operand2 , "int")
  			regtoMem(reg_operand2 , result ,"int")

 		if operator == "int_un-":
 			reg_result = loadintoreg(result , 2 , "int")
 			reg_operand2 = loadintoreg(operand2 , 0 , "int")
 			code.append('\tneg.s $' + reg_result +', $' + reg_operand2)
 			regtoMem(reg_result , result , "int")

 		if operator == "float_un+":
 			reg_operand2 = loadintoreg(operand2 , "float")
  			regtoMem(reg_operand2 , result ,"float")

 		if operator == "float_un-":
 			reg_result = loadintoreg(result , 2 , "float")
 			reg_operand2 = loadintoreg(operand2 , 0 , "float")
 			code.append('\tneg.s $' + reg_result +', $' + reg_operand2)
 			regtoMem(reg_result , result , "float")

#System calls
 		if operator == "syscall":

 			if result == "Scan_int":
 				code.append('\tli $v0'  + ', ' + '5')
 				code.append('\tsyscall')
 				regtoMem('v0' , operand1 , "int")

 			elif result == "Scan_float":
 				code.append('\tli $v0'  + ', ' + '6')
 				code.append('\tsyscall')
 				regtoMem('f0' , operand1 , "float")

 			elif result == "Scan_char":
 				code.append('\tli $v0'  + ', ' + '12')
 				code.append('\tsyscall')
 				regtoMem('v0' , operand1 , "int")

 			elif result == "Print_int":
 				code.append('\tli $v0'  + ', ' + '1')
 				reg = loadintoreg(operand1  , -1 , "int")
 				code.append('\tsyscall')

 			elif result == "Print_float":
 				code.append('\tli $v0'  + ', ' + '2')
 				reg = loadintoreg(operand1 , -1 , "float")
  				code.append('\tsyscall')


 			elif result == "Print_char":
 				code.append('\tli $v0'  + ', ' + '11')
 				reg = loadintoreg(operand1 , -1 , "int")
  				code.append('\tsyscall')


 			elif result == "Print_newline":
 				reg_operand1 = loadintoreg( operand1 , 0 , "int")
 				code.append('newline' + str(newline_count) + ':')
 				code.append('\tble $' + reg_operand1 + ', $0, newline' + str(newline_count + 1)) 				
 				code.append('\tli $v0'  + ', ' + '4')
 				code.append('\tla $a0'  + ', ' + 'newline')
   				code.append('\tsyscall')
   				code.append('\tsub $' + reg_operand1 + ', $' + reg_operand1 + ', 1' )
   				code.append('\tj newline' + str(newline_count))
   				code.append('newline' + str(newline_count + 1) + ':')
   				newline_count += 2

   			elif result == "int_to_float":
   				reg_operand1 = loadintoreg(operand1, 'f8',  "float")
   				code.append('\tcvt.s.w $f8, $f8')
   				regtoMem('f8' , operand1 , "float")

   			elif result == "float_to_int":
   				reg_operand1 = loadintoreg(operand1 , 'f8'  ,  "float")
   				code.append('\tcvt.w.s $f8, $f8')
   				regtoMem('f8' , operand1 , "float")

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

 				if operand2 == "FLOAT":
	 				for i in range(0,len(returnvars)):
	 					loadintoreg(returnvars[i] , "f" + str(i)  , "float")  #Returned in the order or the return
 				
 				else:
	 				for i in range(0,len(returnvars)):
	 					loadintoreg(returnvars[i] , "v" + str(i)  , "int")  #Returned in the order or the return
 				

 				out_count_variables = len(returnvars) - 1


 			symbol_table.set_current_table(symbol_table.get_current_table().prev_table)
 			code += ['\tla $sp, 0($fp)', '\tlw $ra, -8($fp)', '\tlw $fp, -4($sp)' , '\tjr $ra']

 		if operator == "int_PullParam" :
 			#Restoring the symbol table

 			regtoMem("v" + str(out_count_variables) , result , "int") #storing the information in the return parameters to their corresponding addresses
 			out_count_variables -= 1


 		if operator == "float_PullParam" :
 			#Restoring the symbol table
 			regtoMem("f" + str(out_count_variables) , result , "float") #storing the information in the return parameters to their corresponding addresses
 			out_count_variables -= 1


 		
 		if operator == "procedure_call":
 			parameter_count = len(operand2)
 			out_count_variables = len(operand2) - parameter_count
 			width = symbol_table.get_Attribute_Value(operand1 , "width") + 32
 			#sp is going to go down by this measure
 			count = 0 
 			for item in operand2:
 				reg =  loadintoreg(item , 0 ,"int")
 				code.append('\tsw $' + reg + ', ' + str(count*4 - width) + '($sp)')
 				count += 1

 			code.append('\tjal ProcLabel_' + operand1)
 		
 		if operator == "makelabel":
 			code.append(result + ":")

 		if operator == "goto":
 			if operand1 == None:
	 			if isinstance(result , int):
	 				code.append('\tj ' + 'L' + str(result))

	 			else:
	 				code.append('\tj ' + result)
	 		else:
	 			reg_operand1 = loadintoreg(operand1 , 1 , "int")

	 			if isinstance(result , int):
	 				code.append('\tbeq $' + reg_operand1 + ', 1, L' + str(result))

	 			else:
	 				code.append('\tbeq $' + reg_operand1 + ', 1, ' + result)



 		if operator == "blteq":
 			reg_operand1 = loadintoreg(operand1 , 0 , "int")
 			reg_operand2 = loadintoreg(operand2 , 1 , "int")

	 		if isinstance(result , int):
 				code.append('\tble $' + reg_operand1 + ', $' + reg_operand2+ ', L' + str(result))
	 		else:
	 			code.append('\tble $' + reg_operand1 + ', $' + reg_operand2+ ', ' + result)

 		if operator == "bgteq":
 			reg_operand1 = loadintoreg(operand1 , 0 , "int")
 			reg_operand2 = loadintoreg(operand2 , 1 , "int")

	 		if isinstance(result , int):
 				code.append('\tbge $' + reg_operand1 + ', $' + reg_operand2+ ', L' + str(result))
	 		else:
	 			code.append('\tbge $' + reg_operand1 + ', $' + reg_operand2+ ', ' + result)

#and and or
	 	if operator == "and" :
	 		reg_result = loadintoreg(result , 2 , "int")
 			reg_operand1 = loadintoreg(operand1 , 0 , "int")
 			reg_operand2 = loadintoreg(operand2 , 1 , "int")

 			code.append('\tand $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result , "int")

	 	if operator == "or" :
 			reg_result = loadintoreg(result , 2 , "int")
 			reg_operand1 = loadintoreg(operand1 , 0 , "int")
 			reg_operand2 = loadintoreg(operand2 , 1 , "int")

 			code.append('\tor $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)
 			regtoMem(reg_result , result , "int")

#starstar
 		if operator == "starstar" :
			reg_result = loadintoreg(result , 2 , "int")
 			reg_operand1 = loadintoreg(operand1 , 0 , "int")
 			reg_operand2 = loadintoreg(operand2 , 1 ,"int") 	

 			code.append('\tli $' + reg_result + ', 1')
 			code.append('start' + str(target_count) + ":")
 			code.append('\tble $' + reg_operand2 + ', 0, ' + "target" + str(target_count))
 			code.append('\tmul $' + reg_result + ', $' + reg_result + ', $' + reg_operand1)
 			code.append('\tsub $' + reg_operand2 + ', $' + reg_operand2 + ', 1')
 			code.append('\tj start' + str(target_count))
 			code.append("target" + str(target_count) + ":")
 			target_count += 1

 			regtoMem(reg_result , result , "int")

#Comparison Operators

		
		if len(operator.split("_")) >= 2 and operator.split("_")[1] in  ["=" , "/=" , ">" , "<" , ">=" , "<="]:
			my_type = operator.split("_")[0]
			symbol = operator.split("_")[1]

			if (my_type == "float"):
				reg_result = loadintoreg(result , 2 , "int")
 				reg_operand1 = loadintoreg(operand1 , 0 , "float")
 				reg_operand2 = loadintoreg(operand2 , 1 , "float")

 			else:
				reg_result = loadintoreg(result , 2 , "int")
 				reg_operand1 = loadintoreg(operand1 , 0 , "int")
 				reg_operand2 = loadintoreg(operand2 , 1 , "int")


 			if (my_type == "int"):
 				if symbol == "=": fn = 'seq'
 				elif symbol == "/=": fn = 'sne'
 				elif symbol == "<": fn = 'slt'
 				elif symbol == ">": fn = 'sgt'
 				elif symbol == "<=": fn = 'sle'
 				elif symbol == ">=": fn = 'sge'

				code.append('\t' + fn + ' $' + reg_result + ', $' + reg_operand1 + ', $' + reg_operand2)

 			else:
 				if symbol == "=": code.append('\tc.eq.s $' + reg_operand1 + ', $' + reg_operand2)
 				
 				elif symbol == "/=": 
 					code.append('\tc.eq.s $' + reg_operand1 + ', $' + reg_operand2)
		 			code.append('\tbc1t ' + "float" + str(count))
		 			code.append('\tnop')

		 			code.append('\tbc1f ' + "float" + str(count + 1))
		 			code.append('\tnop')

		   			code.append("float" + str(count) + ':')
		  			code.append('\tli $' + reg_result + ', 0')
		   			code.append('\tj float' + str(count + 2))

					code.append("float" + str(count + 1) + ':')
		   			code.append('\tli $' + reg_result + ', 1')
		   			code.append('\tj float' + str(count + 2))

		   			code.append("float" + str(count + 2) + ':')
		   			float_count += 3
		   			count += 3
		   			regtoMem(reg_result , result ,"int")
		   			continue

 				elif symbol == "<" : code.append('\tc.lt.s $' + reg_operand1 + ', $' + reg_operand2)
 				elif symbol == ">" : code.append('\tc.le.s $' + reg_operand2 + ', $' + reg_operand1)
 				elif symbol == "<=": code.append('\tc.le.s $' + reg_operand1 + ', $' + reg_operand2)
 				elif symbol == ">=": code.append('\tc.lt.s $' + reg_operand2 + ', $' + reg_operand1)


 			if (my_type == "float"):
	 			code.append('\tbc1t ' + "float" + str(count))
	 			code.append('\tnop')

	 			code.append('\tbc1f ' + "float" + str(count + 1))
	 			code.append('\tnop')

	   			code.append("float" + str(count) + ':')
	  			code.append('\tli $' + reg_result + ', 1')
	   			code.append('\tj float' + str(count + 2))

				code.append("float" + str(count + 1) + ':')
	   			code.append('\tli $' + reg_result + ', 0')
	   			code.append('\tj float' + str(count + 2))

	   			code.append("float" + str(count + 2) + ':')

	   			float_count += 3
	   			count+=3

 			regtoMem(reg_result , result ,"int")

 	for instr in three_addr_code.get_list():
 		print instr

 	code += ['\nexit:' , '\tli $v0, 10' , '\tsyscall']
 	return code
