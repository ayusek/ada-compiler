#!/usr/bin/env python
import re

def make_ParseTree(file_name) :
	outfile = open(file_name.split('.')[0] + ".dot", 'a')	
	f = open("intermediate_dot",'r')
	
	outfile.write("digraph Parse_tree {\n")
	a = re.compile("Action : Reduce rule")
	
	Dict = {"start_symbol":{"List":[0] , "count":1}}
	for line in reversed(f.readlines()):
	    if (a.match(line)):
	        line = line.split('[')[1].split(']')[0]
	        lhs = line.split("->")[0].replace(" ",'')
	        rhs = line.split("->")[1].split(" ")
	
	        lhstoken = lhs + '__' + str(Dict[lhs]["List"][-1]) + '__'
	        del Dict[lhs]["List"][-1]
	
	        for rhsword in rhs:
	            if (rhsword != ''):
	                if rhsword not in Dict : 
	                    Dict[rhsword] = {"List":[0] , "count":1}
	                    rhstoken = rhsword + "__0__"
	                else: 
	                    count = int(Dict[rhsword]["count"]) 
	                    Dict[rhsword]["List"].append(count)
	                    rhstoken = rhsword + '__' + str(count) + '__'
	                    Dict[rhsword]["count"] = count + 1
	
	                outfile.write("\t\"" + lhstoken + "\"" + "->" + "\"" + rhstoken + "\";\n")
	outfile.write("}\n")
	return



