#!/usr/bin/env python
from three_addrcode_functions import * #Has symbol Table in it
code = []

#we have the current register context with us
def getreg(variable , selector): #0 for operand 1 , 1 for operand 2, 2 for result
	regname = 't' + str(selector)
	return regname

def loadintoreg(regname , variable , selector = 0):
	reg = getreg(variable , selector)

	if isinstance(variable,int):
		code.append('\tli $' + reg + ', ' + str(x))

	elif isinstance(variable , float):
		code.append('\tli.s $' + reg + ', ' + str(x))


	elif '\'' in variable: #character
		code.append('\tli $' + reg + ', ' + x)

	elif '(' in variable:
		variable = variable.split('(')[0]
		offset_variable  = (variable.split('(')[1]).split(')')[0]
		temp_reg = getreg(offset_variable , 3)
		code.append('\tli $'+ reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')))
		code.append('\tadd $' + reg + ', $sp, $' + reg)
		code.append('\tlw $' + temp_reg +  ", " + str(symbol_table.get_Attribute_Value(offset_variable , 'offset')))
		code.append('\tadd $' + reg + ', $'+ temp_reg +', $' + temp_reg)
		code.append('\tlw $' + reg + ', ($' + temp_reg +')')

	elif isinstance(variable , str) :	
		code.append('\tlw $'+ reg + ', ' + str(symbol_table.get_Attribute_Value(variable,'offset')) + '($sp)')

	else :
		print "Unknow type of argument passed " + variable
		reg = None

	return reg #reg not contains its value

def regtoMem(reg , variable):
	if '(' in variable: #array support

	else:
		

#Returns a string of instructions
def TAC2spim( three_addr_code , main_procedure_name):

	global symbol_table
	global code

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
 			reg_res = getreg(result , 2 )
 			reg_op1 = getreg(operand1 , 0)
 			reg_op2 = getreg(operand2 , 1)


 		if operator  == "proc_label":
 			code.append("ProcLabel_" + result + ":")

 			width = symbol_table.get_Attribute_Value(result , "width")
 			#Currently in the symbol table of the senior
 			symbol_table.set_current_table(symbol_table.get_Attribute_Value(result , "SymbolTable"))

 			code += [ '\tsw $fp, -4($sp)' , '\tsw $ra, -8($sp)' , '\tla $fp, 0($sp)' , '\tla $sp, -' + str(width) + '($sp)']

 		if operator == ":=":
 			reg = loadintoreg(operand1)
 			regtoMem(reg , result)
 			#Received three registers

 	for instr in three_addr_code.get_list():
 		print instr

 	return code
