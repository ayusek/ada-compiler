#!/usr/bin/env python
import sys
import lex
import re
from  adaTokens import *

#Some Regularexpressions
contains_text = re.compile("[A-Za-z]+")

#Scanning the file name
if (len(sys.argv) == 1):
    file_name =raw_input( "Give an Ada file to lex: ")
else:
    file_name = sys.argv[1]

try:
    lexer = lex.lex()
    with open(file_name) as fp:#opening file
        data = fp.read()
        lexer.input(data)
        datalist = data.split('\n')
        i = 0
        tokstring = ""

        while 1:
            old_line = lexer.lineno
            tok = lex.token()
            if not tok : break
            
            if (lexer.lineno != old_line) :
                print datalist[i]  + "--" + tokstring
                i = i + 1
                tokstring = ""
                while (datalist[i] == '') :
                    print('')
                    i = i + 1
            if (str(tok.value) in literals): 
                tokstring = tokstring + " " +  "'" + str(tok.type) + "'"
            else:
                tokstring = tokstring + " " + str(tok.type)

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissionsi!"

    
    
