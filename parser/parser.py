#!/usr/bin/env python
import sys
import lex
import yacc
import re
from  adaTokens import *
from parser_functions import *

parser = yacc.yacc(start = 'start_symbol', debug = True)

while True:
    try:
        s = raw_input('calc > ')
    except EOFError:
	    break
    if not s: continue
	result = parser.parse(s)
	print (result)
 

'''
#Scanning the file name
if (len(sys.argv) == 1):
    file_name =raw_input( "Give an Ada file to parse: ")
else:
    file_name = sys.argv[1]

try:
    lexer = lex.lex()

    with open(file_name) as fp:#opening file
        data = fp.read()
        parser = yacc.yacc(start = 'start_symbol', debug = True)
 
        
        lexer.input(data)
        result = parser.parse(data)
#        result = yacc.parse(data , start = 'start_symbol')
        print("output is :",result)
    
except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissions!"
'''
