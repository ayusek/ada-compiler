#!/usr/bin/env python
import sys
import lex
import re
from  adaTokens import *

#Scanning the file name
if (len(sys.argv) == 1):
    file_name =raw_input( "Give an Ada file to lex: ")
else:
    file_name = sys.argv[1]

try:
    lexer = lex.lex()
    with open(file_name) as fp:#opening file
        data = fp.read()
        data += '\n'
        lexer.input(data)
        datalist = data.split('\n')
        tokstring = ""
        old_line = lexer.lineno
        #print datalist
        #Prininting it line by line
        
        for tok in lexer:
            if(tok.lineno != old_line) :
                print datalist[old_line-1] + "--" + tokstring
                tokstring = ""
                for i in xrange(old_line,tok.lineno-1):
                    print datalist[i]
                old_line=tok.lineno
            if(str(tok.type) in literals):
                tokstring += " " + "'" +  str(tok.type) + "'"
            else:    
                tokstring += " " + str(tok.type)
   
        print datalist[old_line-1] + "--" + tokstring
        tokstring = ""
        for i in xrange(old_line,tok.lineno-1):
            print datalist[i]
        old_line=tok.lineno
   
    if error_list : 
        print  "=====ERRORS====="
        print '\n'.join(error_list), 

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissionsi!"

    
    
