#!/usr/bin/env python

from symbol_table import *


Debug1 = False
Debug2 = True

symbol_table = SymbolTable()

#Width for standard data types
width= {'INT':4, 'FLOAT':8, 'CHAR':1, 'BOOL':4} #8- bit characters 

symbol_table.createSym('integer',{'type': 'INT', 'lexeme':'integer', 'istype':True})
symbol_table.createSym('float',{'type': 'FLOAT', 'lexeme':'float', 'istype':True})
symbol_table.createSym('character',{'type': 'CHAR', 'lexeme':'character', 'istype':True})
symbol_table.createSym('string',{'type': 'STRING', 'lexeme':'string', 'istype':True})
symbol_table.createSym('boolean',{'type': 'BOOL', 'lexeme':'boolean', 'istype':True})

temp_counter = 0 

def get_tempno():
	global temp_counter
	temp_counter += 1
	return temp_counter


def get_temp(type): #Makes a new temperory variable and then returns its name
	name = 't' + str(get_tempno())
	symbol_table.createSym(name , {"type" : type , "offset" : symbol_table.get_width() , "lexeme" : name , "value" : None})
	symbol_table.change_width(width(type))
	return name

# 3 Address code list structure
class Structure:
    def __init__(self):
        self.next_instr_no = 0 
        self.List = []

    def emit(self, result , operand1 , operator , operand2):
    	self.List.append(str(self.next_instr_no) + " : " + result + str(operand1) + str(operator) + str(operand2))
    	self.next_instr_no += 1

    def get_next_instr_no(self):
    	return  self.next_instr_no

three_addr_code = Structure()




