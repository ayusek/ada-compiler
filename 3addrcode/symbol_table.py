#!/usr/bin/env python

#Symbol Table has been designed for data-types, Identifiers and procedures 

#Class Table is a standard symbol table
# It is a dictionary of dictionaries.. 
#

#Width for standard data types
width= {'INT':4, 'FLOAT':8, 'CHAR':1, 'BOOL':4} #8- bit characters 

def get_type_width(name):
	global width 
	if (isinstance(name , str)):
		return width[name]
	else:
		if(name["type"] in width):
			return width[name["type"]]
		else:
			if "width" in name:
				return name["width"]
			else:
				print "[Data Type] Error : Width of the object is not know while assigning"
				return 0


def procedure_name(name , var_List = None):
	str = ""
	str = str + name.lower()
	#Need to Add Overloading features here
	return str

class Table:
	def __init__(self , prev = None):
		self.Hash = {} # Empty Dictionary
		self.width =  0
		self.paramwidth = 0 
		self.prev_table = prev #A Table Block

	def createSym(self, name , Attribute_List):
		name = name.lower() # Ada is case insensitive
		if name in self.Hash:
			print 'Error : Symbol -' + name + '- Already presnt in the symbol table - ' + str(self)   # may need to remove this self

		else :
			self.Hash[name] = {} # An empty dictionary
			for item in Attribute_List :
				self.Hash[name][item] = Attribute_List[item]


	#Update/Insert
	def updateSym(self, name , Attribute_Name , Value): # returns a boolean if it was a successful update
		name = name.lower()

		current_table = self

		while current_table != None:
			if name in current_table.Hash:
				(current_table.Hash[name])[Attribute_Name] = Value # Adding Correcponding value
				return True
			current_table = current_table.prev_table

		return False


	def get_Attribute_Value_in_Block(self, name , Attribute_Name): 
		name = name.lower()

		#Dictionary's give errors if stuff not found
		try :
			return self.Hash[name][Attribute_Name]
		except :
			return None

	def get_Attribute_Value(self , name , Attribute_Name):
		name = name.lower()

		current_table = self

		while current_table != None :
			value = current_table.get_Attribute_Value_in_Block(name , Attribute_Name)
			if (value != None) :
				return value
			else:
				current_table = current_table.prev_table

		return None


	def locate_Symbol_in_this(self , name):
		name = name.lower()
		if name in self.Hash:
			return True
		else:
			return False

	def locate_Symbol(self , name) :
		name = name.lower()

		current_table = self

		while current_table != None :
			if current_table.locate_Symbol_in_this(name):
				return True
			else:
				current_table = current_table.prev_table

		return False

	def get_Hash_Table(self):
		return self.Hash


	def get_row(self , name) :
		name = name.lower()
		current_table = self 

		while(current_table != None):
		 	if(current_table.locate_Symbol_in_this(name) == True):
		 		return current_table.Hash[name]
			
			current_table = current_table.prev_table

		return None
		
		

	# Currently only prints this table
	# CAN IMPROVE IT

	def print_Symbol_Table(self):
		print "********* Printing the Symbol Table " + str(self) + "*********"
		for item in self.Hash:
			if "SymbolTable" in self.Hash[item]:
				print "+++++++++++++++++++++++++++++++++++++++"
				print "printing the sub symbol table for " +  item 
				print "+++++++++++++++++++++++++++++++++++++++"
				self.Hash[item]["SymbolTable"].print_Symbol_Table()
				print "---------------------------------------"
			print item + " ==> " + str(self.Hash[item])



	#Width Opeations to be done on the stack 
	def get_width(self):
		return self.width

	def change_width(self, change) :
		self.width = self.width + change

	def get_paramwidth(self):
		return self.paramwidth

	def change_paramwidth(self , change):
		self.paramwidth = self.paramwidth + change


# Links all these tables and then brings them into order. 
# Maintains the current symbol table which is linked to other guys and operate over it and traverse over it.
# We would operate on the level of this SymbolTable.

class SymbolTable:
	def __init__(self):
		self.symbol_table = Table()

	def createSym(self, name , Attribute_List):
		self.symbol_table.createSym(name , Attribute_List)

		#Update/Insert
	def updateSym(self, name , Attribute_Name , Value): # returns a boolean if it was a successful update
		return self.symbol_table.updateSym(name , Attribute_Name , Value)

		# Searches for Attribute Value throughtout the hierarchy
	def get_Attribute_Value(self , name , Attribute_Name):
		return self.symbol_table.get_Attribute_Value(name , Attribute_Name)

	def locate_Symbol_in_this(self , name):
		return self.symbol_table.locate_Symbol_in_this(name)

	def locate_Symbol(self , name) :
		return self.symbol_table.locate_Symbol(name)

	def get_Hash_Table(self):
		return self.symbol_table.get_Hash_Table()

	def get_row(self , name) :
		return self.symbol_table.get_row(name)


	def print_Symbol_Table(self):
		self.symbol_table.print_Symbol_Table()


	#Width Opeations to be done on the stack 
	def get_width(self):
		return self.symbol_table.get_width()

	def change_width(self, change) :
		self.symbol_table.change_width(change)

	def get_paramwidth(self):
		return self.symbol_table.get_paramwidth()

	def change_paramwidth(self , change):
		self.symbol_table.change_paramwidth(change)



	#May Not be Required
	def get_current_table(self):
		return self.symbol_table

	def set_current_table(self , table_Object):
		self.symbol_table = table_Object


	# Define  new Table and the change to it
	def begin_scope(self):
		new_table = Table(self.symbol_table)
		self.symbol_table = new_table
		return self.symbol_table


	def end_scope(self):
		self.symbol_table = self.symbol_table.prev_table



		#Only Called after creating a new scope 
		# Current Symbol table = Procedure symbol Table

		#I have a dictionary corresponding to each variable which stores information about it like its type, etc.

		#varlist is a list of dictionaries for each variable of dictionaries
	def declare_Procedure(self , name , var_List):
		old_name = name
		name = procedure_name(name , var_List)

		#Inserting Name into the parent and generating Links with the Parent
		if self.symbol_table.prev_table == None : #Should Not happen if scope was started first
			print "Function not Defined within a global scope - Some Problem with the declaration of " + "old_name"
		else :
			#Make an entry for the procedure and store the pointer
			self.symbol_table.prev_table.createSym(name , {"isprocedure" : True , "SymbolTable" : self.symbol_table,  "var_List" : var_List , "lexeme" : old_name}) # in_List and out_List are not required as such
			
			for item in var_List :
				self.symbol_table.createSym(item["name"] , item["dictionary"])
				self.symbol_table.updateSym(item["name"] , "offset" , self.symbol_table.get_width())
				self.symbol_table.change_width(get_type_width(item["dictionary"]["type"]))

	

'''
st = SymbolTable()
#new_table = Table()
st.createSym('ayush' , {'age' : 19 , 'sex' : 'M' , 'room' : 'F208' })

dict = {'gender': {'out': True, 't': 'String', 'in': False}, 'name': {'out': True, 't': 'string', 'in': True}}

st.begin_scope()
st.declare_Procedure("person" , dict)
st.end_scope()

st.begin_scope()
st.declare_Procedure("person1" , dict)
st.end_scope()

st.print_Symbol_Table()
'''