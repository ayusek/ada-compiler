#!/usr/bin/env python
import re

def clean(word) :
	return { 
        '&': "ampersant",
        '(': "open_bracket",
	')': "close_bracket",
	'*': "star",
	'+': "plus",
	',': "comma",
	'-': "hyphen",
	'.': "dot",
	'/': "forward_slash",
	':': "colon",
	';': "semi_colon",
	'<': "less",
	'=': "equal",
	'>': "more",
    "<empty>" : "empty",
	}.get(word,word)

def make_ParseTree(file_name) :
	outfile = open(file_name.split('.')[0] + ".dot", 'w')	
	f = open("intermediate_dot",'r')
	
	outfile.write("digraph Parse_tree {\n")
	a = re.compile("Action : Reduce rule")
	
	Dict = {"start_symbol":{"List":[0] , "count":1}}
	for line in reversed(f.readlines()):
	    if (a.match(line)):
	        line = line.split('[')[1].split(']')[0]
	        lhs = line.split("->")[0].replace(" ",'')
	        rhs = line.split("->")[1].split(" ")
	        lhstoken =  clean(lhs) +  str(Dict[lhs]["List"][-1])
	        del Dict[lhs]["List"][-1]
		outfile.write("\t" + lhstoken + '[ label =' + '\"' + lhs  + '\"''];\n')
	        for rhsword in rhs:
	            if (rhsword != ''):
	                if rhsword not in Dict : 
	                    Dict[rhsword] = {"List":[0] , "count":1}
	                    rhstoken = clean(rhsword) + "0"
	                else: 
	                    count = int(Dict[rhsword]["count"]) 
	                    Dict[rhsword]["List"].append(count)
	                    rhstoken =  clean(rhsword) + str(count)
	                    Dict[rhsword]["count"] = count + 1
	
                    	outfile.write("\t" + rhstoken + '[ label =' + '\"' + rhsword  + '\"''];\n')
	                outfile.write("\t" + lhstoken  + "->" + rhstoken + ";\n")
	outfile.write("}\n")
	return



