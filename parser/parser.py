#!/usr/bin/env python
import sys
import lex
import yacc
import re
import sys

from  adaTokens import *
from parser_functions import *
from make_out import *

old_stderr = sys.stderr


parser = yacc.yacc(start = 'start_symbol', debug = True)


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
        sys.stderr = open("intermediate_dot" , 'w')
        result = parser.parse(data , debug = 1)
        sys.stderr = old_stderr
        make_ParseTree(file_name)

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissions!"

