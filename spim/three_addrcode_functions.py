#!/usr/bin/env python

from symbol_table import *


Debug1 = False
Debug3 = False


symbol_table = SymbolTable()



symbol_table.createSym('integer',{'type': 'INT', 'lexeme':'integer', 'istype':True , 'width' : 4})
symbol_table.createSym('float',{'type': 'FLOAT', 'lexeme':'float', 'istype':True , 'width' : 8})
symbol_table.createSym('character',{'type': 'CHAR', 'lexeme':'character', 'istype':True , 'width' : 1})
#symbol_table.createSym('string',{'type': 'STRING', 'lexeme':'string', 'istype':True , 'width' : None})
symbol_table.createSym('boolean',{'type': 'BOOL', 'lexeme':'boolean', 'istype':True , 'width' : 4})

temp_counter = 0  



def get_tempno():
	global temp_counter
	temp_counter += 1
	return temp_counter


def get_temp(type): #Makes a new temperory variable and then returns its name
	name = '_t' + str(get_tempno())
	symbol_table.createSym(name , {"type" : type , "offset" : symbol_table.get_width() , "lexeme" : name , "value" : None , "width" : get_type_width(type)})
	symbol_table.change_width(get_type_width(type))
	return name

# 3 Address code list structure
class Structure:
    def __init__(self):
        self.next_instr_no = 0 
        self.List = []

    def emit(self, result , operand1 , operator , operand2):
    	self.List.append([self.next_instr_no , result , operand1 , operator , operand2])
    	self.next_instr_no += 1

    def get_next_instr_no(self):
    	return  self.next_instr_no

    def print_structures(self):
    	print "========== Three Address Code ==============="
    	for i in self.List:
    		print i

    def get_list(self):
        return self.List


three_addr_code = Structure()

def makeList(i):
	return [i]

def merge(L1 , L2):
	return L1 + L2

def backpatch(L1 , instr_number):
    for item in L1:
        mylist = three_addr_code.List[item]
        for i in range(0,5):
            if(mylist[i] == None):
                mylist[i] = str(instr_number)
                break






