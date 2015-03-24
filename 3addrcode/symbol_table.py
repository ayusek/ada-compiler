#!/usr/bin/env python

#Symbol Table has been designed for data-types, Identifiers and procedures 

#Class Table is a standard symbol table
# It is a dictionary of dictionaries.. 
#

class Table:
	def __init__(self):
		self.Hash = {} # Empty Dictionary

	def createSym(self, name):
		name = name.lower() # Ada is case insensitive
		if name in self.Hash:
			print 'Error : Symbol -' + name + '- Already presnt in the symbol table - ' + str(self)   # may need to remove this self

		else :
			self.Hash[name] = {} # An empty dictionary

	def locate_Symbol(self , name):
		name = name.lower()
		if name in self.Hash:
			return True
		else:
			return False

	#Update/Insert
	def updateSym(self, name , Attribute_Dictionary): # returns a boolean if it was a successful update
		name = name.lower()
		try :
			for item in Attribute_Dictionary :
				(self.Hash[name])[item] = Attribute_Dictionary[item] # Adding Correcponding value
			return True

		except :	
			return False

	def get_Attribute_Value(self, name , Attribute_name): 
		name = name.lower()
		#Dictionary's give errors if stuf not found
		try :
			return self.Hash[name][Attribute_value]
		except :
			return none

	def get_Complete_Table(self):
		return self.Hash

	def print_Symbol_Table(self):
		print "Printing the Symbol Table " + str(self)
		print "Attribute ==> Value"
		for item in self.Hash:
			print item + " ==> " + self.Hash[item]

	

new_table = Table()
new_table.print_Symbol_Table()