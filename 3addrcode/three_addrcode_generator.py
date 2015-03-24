#!/usr/bin/env python

from  parser import * 

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
        result = parser.parse(data)# , debug = 1)
	print three_addr_code.List

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissions!"
