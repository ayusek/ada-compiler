#!/usr/bin/env python

from symbol_table import *


symbol_table = SymbolTable()

# 3 Address code list structure
class Structure:
    def __init__(self):
        self.next_instr_no = 0 
        self.List = []

three_addr_code = Structure()


