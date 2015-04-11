


def threeaddr_to_spim(three_addr_code,main_proc_name):
	
	current_env = globalitems.symbol_table.get_attribute_value(str(main_proc_name), 'env_ptr')
	globalitems.symbol_table.set_env(current_env)
	
	assembly_code="#Ada V3\n\n";
	assembly_code = assembly_code + '.data\n'
	assembly_code = assembly_code + '\tnewline : .asciiz "\\n" \n'
	for each in globalitems.symbol_table.get_current_table() :
		flag=False
		if globalitems.symbol_table.get_attribute_value(each,'isprocedure')==True:
			continue
		if globalitems.symbol_table.get_attribute_value(each,'class').lower()=='integer':
			size='4'
		elif globalitems.symbol_table.get_attribute_value(each, 'class').lower()=='float':
			size='8'
		elif globalitems.symbol_table.get_attribute_value(each, 'class').lower()=='char':
			size='1'
		elif globalitems.symbol_table.get_attribute_value(each, 'class').lower()=='boolean':
			size='4'
		else:
			flag = True
		if not flag:
			assembly_code = assembly_code + '\t' + each + ": .space " + size + '\n'
		if globalitems.symbol_table.get_attribute_value(each, 'class').lower()=='character':
				assembly_code = assembly_code + '\t\t' + ".align 2" + '\n'
				
	
	print "\n\n----------------------Current Environment is----------------", current_env.print_table()
	current_env_stack = []
	assembly_code+='\n'
	
	assembly_code+='.text\nmain:\n'
	assembly_code+='\tjal L'+str(main_proc_name)+'\n'
	assembly_code+='\tla $sp, 0($sp)\n'
	assembly_code+='\tj exit\n'
	
	param_count=0
	outvar_call = []
	for instr in three_addr_code:
		op=instr.op
		instr_code=""
			
		elif op=='goto':
			if(instr.result!=None):
				instr_code += '\tj ' + 'L' + str(instr.result)
			elif(instr.result==None):
				instr_code += '\tj ' + 'exit'
			
		elif op in ['beq','bleq','bgeq','bgreater','bless','bneq']:			
			instr_code += LoadInstr(instr.arg1, 't0', current_env)
			instr_code += LoadInstr(instr.arg2, 't1', current_env)
			
			if op == 'beq':
				instr_code += '\tbeq $t0, $t1, ' + 'L' + str(instr.result) + '\n'
			elif op == 'bleq':
				instr_code += '\tble $t0, $t1, ' + 'L' + str(instr.result) + '\n'
			elif op == 'bgeq':
				instr_code += '\tbge $t0, $t1, ' + 'L' + str(instr.result) + '\n'
			elif op == 'bgreater':
				instr_code += '\tbgt $t0, $t1, ' + 'L' + str(instr.result) + '\n'
			elif op == 'bless':
				instr_code += '\tblt $t0, $t1, ' + 'L' + str(instr.result) + '\n'
			elif op == 'bneq':
				instr_code += '\tbne $t0, $t1, ' + 'L' + str(instr.result) + '\n'

#======================procedural calling=======================
			
		elif op=='param':
			param_count=param_count+1
			instr_code += LoadInstr(instr.arg1, 't0', current_env)
			instr_code += '\tsw $t0, -'+ str(param_count*4) +'($sp)\n'
			if (instr.arg2 == 'out'):
				outvar_call = [instr.arg1] + outvar_call;
		
		elif op=='call':					#arg2 is number of parameters
			param_count = 0
			instr_code += '\tla $sp, -' + str(4*instr.arg2) + '($sp)\n'
			instr_code += '\tjal ' + 'L' + instr.arg1 + '\n'
			instr_code += '\tla $sp, ' + str(4*instr.arg2) + '($sp)\n'
		
			if len(outvar_call) > 0:
				count_callout=0
				for each in outvar_call:
					instr_code += '\tsw $v'+str(count_callout) + ', ' + str(current_env.get_attribute_value(each,'offset')) + '($sp)\n'
					count_callout+=1
			outvar_call=[]
			
		elif op=='proc_begin':	
			instr_code=instr_code+'L'+instr.arg1+':'
			while not current_env.is_present_current_block(instr.arg1):
				current_env = current_env.prev_env
			
			current_env = current_env.get_attribute_value(instr.arg1, 'env_ptr')	#getting into symbol table env of this procedure
			
			instr_code += '\tsw $fp, -4($sp)\n'
			instr_code += '\tsw $ra, -8($sp)\n'
			instr_code += '\tla $fp, 0($sp)\n'
			instr_code += '\tla $sp, -' + str(32) + '($sp)\n'			#fixing at 32 not..instr.arg1+8
		
		elif op=='return' :			# here output variable is passed .. call by ref (3rd one)
			#no need to load to v0
			outvar_return=[]
			count_return=0
			if instr.arg1 != None:
				outvar_return = (instr.arg1).split(',')
				for each in outvar_return:
					instr_code += LoadInstr(each, 'v'+str(count_return), current_env)	
					count_return+=1
			current_env = current_env.prev_env		#restore env
			instr_code += '\tla $sp, 0($fp)\n'
			instr_code += '\tlw $ra, -8($fp)\n'
			instr_code += '\tlw $fp, -4($sp)\n'
			instr_code += '\tjr $ra\n'
			
#===================================================================		

		elif op=='syscall':
			if instr.arg1 == 'print_int':
				instr_code += '\tli $v0'  + ', ' + '1' + '\n'
				instr_code += LoadInstr(instr.arg2, 't0', current_env)
				instr_code += '\tmove $a0'  + ', $t0 \n'
			elif instr.arg1 == 'print_char':
				instr_code += '\tli $v0'  + ', ' + '11' + '\n'
				instr_code +=  LoadInstrChar(instr.arg2, 'a0', current_env)
			elif instr.arg1 == 'print_newline':
				instr_code += '\tli $v0'  + ', ' + '4' + '\n'
				instr_code += '\tla $a0'  + ', ' + 'newline' + '\n'
			elif instr.arg1 == 'print_float':
				instr_code += '\tli $v0'  + ', ' + '2' + '\n'
				instr_code += '\tla $f12'  + ', ' + instr.arg2 + '\n'
			elif instr.arg1 == 'print_string':
				instr_code += '\tli $v0'  + ', ' + '4' + '\n'
				instr_code += '\tla $a0'  + ', ' + instr.arg2 + '\n\tla $sp, 4($sp)\n'
			elif instr.arg1 == 'exit':
				instr_code += '\tli $v0'  + ', ' + '10' + '\n'
			instr_code += '\tsyscall\n'	

		assembly_code = assembly_code + instr_code + '\n'
	assembly_code += 'exit:\n'
	assembly_code += '\tli $v0, 10\n\tsyscall'
	print_spim_code(assembly_code)
	return assembly_code
	

def LoadInstrFloat(x,reg,env):
	if type(x)==type(0):				
		return '\tli $' + reg + ', ' + str(x) + '\n'
	elif type(x)==type(""):
		return '\tlw $'+ reg + ', ' + str(env.get_attribute_value(x,'offset')) + '($sp)'+ '\n'
	else:
		return ''
		
def LoadInstrChar(x,reg,env):
	if '\'' in x:
		return '\tli $' + reg + ', ' + x + '\n'
	else :
		return '\tlb $'+ reg + ', ' + str(env.get_attribute_value(x,'offset')) + '($sp)'+ '\n'

def StoreInstrFloat(x,reg,env):
	return '\tsw $' + reg + ', ' + str(env.get_attribute_value(x,'offset')) + '($sp)\n'

def print_spim_code(assembly_code):
	fpout=open('Spim_Code.asm','w')
	fpout.write('# Full Spim Assembly Code is here.\n\n')
	fpout.write(assembly_code)
	print '\ncode written to : Spim_Code.asm\n'
	fpout.close()
Status API Training Shop Blog About
© 2015 GitHub, Inc. Terms Privacy Security Contact
