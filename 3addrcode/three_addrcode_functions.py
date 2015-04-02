#!/usr/bin/env python

from symbol_table import *


Debug1 = False
Debug2 = False
Debug3 = False


symbol_table = SymbolTable()

#Width for standard data types
width= {'INT':4, 'FLOAT':8, 'CHAR':1, 'BOOL':4} #8- bit characters 

symbol_table.createSym('integer',{'type': 'INT', 'lexeme':'integer', 'istype':True , 'width' : 4})
symbol_table.createSym('float',{'type': 'FLOAT', 'lexeme':'float', 'istype':True , 'width' : 8})
symbol_table.createSym('character',{'type': 'CHAR', 'lexeme':'character', 'istype':True , 'width' : 1})
symbol_table.createSym('string',{'type': 'STRING', 'lexeme':'string', 'istype':True , 'width' : None})
symbol_table.createSym('boolean',{'type': 'BOOL', 'lexeme':'boolean', 'istype':True , 'width' : 4})

temp_counter = 0  

def get_type_width(name):
	global width 
	if (isinstance(name , str)):
		return width[name]
	else:
		if(name["type"] in width):
			return width[name["type"]]
		else:
			if "width" in name:
				return name["width"]
			else:
				print "[Data Type] Error : Width of the object is not know while assigning"
				return 0


def get_tempno():
	global temp_counter
	temp_counter += 1
	return temp_counter


def get_temp(type): #Makes a new temperory variable and then returns its name
	name = '_t' + str(get_tempno())
	symbol_table.createSym(name , {"type" : type , "offset" : symbol_table.get_width() , "lexeme" : name , "value" : None})
	symbol_table.change_width(get_type_width(type))
	return name

# 3 Address code list structure
class Structure:
    def __init__(self):
        self.next_instr_no = 0 
        self.List = []

    def emit(self, result , operand1 , operator , operand2):
    	self.List.append(str(self.next_instr_no) + " : " + str(result) + " " + str(operand1) + " "+ str(operator) + " "+ str(operand2))
    	self.next_instr_no += 1

    def get_next_instr_no(self):
    	return  self.next_instr_no

    def print_structures(self):
    	print "========== Three Address Code ==============="
    	for i in self.List:
    		print i

three_addr_code = Structure()

def makeList(i):
	return [i]

def merge(L1 , L2):
	return L1 + L2

def backpatch(L1 , instr_number):
	for item in L1:
		three_addr_code.List[item] += "back_patched with" + str(instr_number)






