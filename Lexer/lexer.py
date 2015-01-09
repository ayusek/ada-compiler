#!/usr/bin/env python
import sys
import lex
from  adaTokens import *

#Scanning the file name
if (len(sys.argv) == 1):
    file_name =raw_input( "Give an Ada file to lex: ")
else:
    file_name = sys.argv[1]

try:
    lexer = lex.lex()
    with open(file_name) as fp:#opening file
        for line in fp:
            line = line.rstrip()
            lexer.input(line)
            tokens = '' 
            while 1:
                tok = lex.token()
                if not tok: break
                tokens += " " + "\'" + str(tok.type) + "\'"

            print(line + "\t --" + tokens)  
    
except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissionsi!"

    
    
