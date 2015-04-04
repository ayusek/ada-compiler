#!/usr/bin/env python
#!/usr/bin/env python

from three_addrcode_functions import *
from copy import deepcopy

import sys
import lex
import yacc
import re
import sys

from  adaTokens import *


success = True

def p_start_symbol(p):
    '''start_symbol : compilation
        '''
    p[0]=p[1]
    global success
    if success : symbol_table.print_Symbol_Table()

    if (Debug1) : print "Rule Done: 1"


#*****************************
def p_pragma(p):
    '''pragma  : PRAGMA IDENTIFIER ';'
       | PRAGMA simple_name '(' pragma_arg_s ')' ';'
    '''
    if (Debug1) : print "Rule Declared: 2"


def p_pragma_arg_s(p):
    '''pragma_arg_s : pragma_arg
       | pragma_arg_s ',' pragma_arg
    '''
    if (Debug1) : print "Rule Declared: 3"


def p_pragma_arg(p):
    '''pragma_arg : expression
       | simple_name ARROW expression
    '''
    if (Debug1) : print "Rule Declared: 4"


def p_pragma_s(p):
    '''pragma_s :
       | pragma_s pragma
    '''
    if (Debug1) : print "Rule Declared: 5"

#*****************************

def p_decl(p):
    '''decl    : object_decl
       | number_decl
       | type_decl
       | subtype_decl
       | subprog_decl    
       | pkg_decl
       | task_decl
       | prot_decl
       | exception_decl
       | rename_decl
       | generic_decl
       | body_stub
       | error ';'
    '''
    if (Debug1) : print "Rule Partially Done: 6"

    #***** handle SubPrograms Seperately **************
    p[0] = p[1] #Checking Done, emits done, Carrying Attributes

def p_object_decl(p):
    '''object_decl : def_id_s ':' object_qualifier_opt object_subtype_def init_opt ';'
    '''
    if (Debug2) : print "Declare Statement"
    if (Debug1) : print "Rule Declared: 7"

    if len(p[1])  == 0 :
        print "[Object Declaration] Error at line " + str(p.lineno(1)) + " : No objects to declare"
        p_error(p)

    if(p[4] == None):
        print "[Object Declaration] Error at line " + str(p.lineno(1)) + " : Type not given"
        p_error(p)

    elif(p[4]["type"] == None): #May convert it to the symbol table
        print "[Object Declaration] Error at line " + str(p.lineno(1)) + " : Type is not defined"
        p_error(p)

    else:
        if(p[5] != None) : 
            p[0] = deepcopy(p[5]) #Carry's Other attributes like nextlist , etc
            if (p[4]["type"] != p[5]["type"]): #Assuming Both to be in the lower case
                print "[Object Declaration] Error at line " + str(p.lineno(3)) + " : Type mismatch in initialization"
                p_error(p)


        #P[1] is a list of identifiers
        for item in p[1]:
            item_lexeme = item
            item = item.lower()
            flag = True

            #checking Presence in Reserved Set or in the current symbol table

            if item in reserved : 
                flag = False
                print "[Object Declaration] Error at line " + str(p.lineno(1)) + " : Object " + item + " is a reserved keyword"
                p_error(p)

            if symbol_table.locate_Symbol_in_this(item):
                flag = False
                print "[Object Declaration] Error at line " + str(p.lineno(1)) + " : Object " + item + " has been already defined in this scope"
                p_error(p) # This function returns back

            if (flag == True) :
                if (p[4]["isarray"] == True):
                    if (Debug2 ) : print "******* INSERTED " + item
                    symbol_table.createSym(item , p[4]) # I will ensure that p[4] is a dictionary having type information
                    symbol_table.updateSym(item , "lexeme" , item_lexeme)
                    #symbol_table.updateSym(item , "offset" , symbol_table.get_width())
                    #symbol_table.change_width(get_type_width(p[4]["Base_Type"])) #Has been set up while evaluating for p[4]
                    

                    if (p[5] != None):
                        print "[Object Declaration] Error at line " + str(p.lineno(1)) + " : Object" + item + " is an array. Initialization of arrays not yet allowed"
                        p_error(p)
                else: #isarray is false
                    #Variables Declared
                    if (Debug2):  print item + " Inserted"
                    symbol_table.createSym(item , p[4]) # I will ensure that p[4] is a dictionary having type information
                    symbol_table.updateSym(item , "lexeme" , item_lexeme)
                    symbol_table.updateSym(item , "offset" , symbol_table.get_width())
                    symbol_table.change_width(get_type_width(p[4])) #Has been set up while evaluating for p[4]

                    if(p[5] != None):
                        if (symbol_table.get_Attribute_Value(item , "isconstant")):
                            print "[Object Declaration] Error at line " + str(p.lineno(1)) + " : Object" + item + " is a constant and can not be assigned"

                        else :
                            if(Debug2) : print "Emitting 3addrcode"
                            three_addr_code.emit(item , p[5]["value"] , ":=" ,  None)

#List of Names
def p_def_id_s(p):
    '''def_id_s : def_id
       | def_id_s ',' def_id
    '''
    if (Debug1) : print "Rule Done: 8"
    if (len(p) == 2):
        p[0] = [p[1]]
    else :
        p[0] = p[1] + [p[3]]

def p_def_id(p):
    '''def_id  : IDENTIFIER
    '''
    if (Debug1) : print "Rule Done: 9"
    p[0] = p[1]

def p_object_qualifier_opt1(p):
    '''object_qualifier_opt :
       | ALIASED
       | ALIASED CONSTANT
    '''
    if (Debug1) : print "Rule Declared: 10a"
    if (len(p) == 2):
        p[0] = {"isconstant" : False , "isaliased" : True , "isnull" : False}
    elif (len(p) == 3):
        p[0] = {"isconstant" : True , "isaliased" : True , "isnull" : False}
    else:
        p[0] = {"isconstant" : False , "isaliased" : False , "isnull"  : True}

def p_object_qualifier_opt2(p):
    '''object_qualifier_opt : CONSTANT
    '''
    p[0] = {"isconstant" : True , "isaliased" : False , "isnull" : False}
    if (Debug1) : print "Rule Declared: 10b"

def p_object_subtype_def(p):
    '''object_subtype_def : subtype_ind
       | array_type
    '''
    if (Debug1) : print "Rule Declared: 11"
    p[0] = p[1] #Carry the type information forward

def p_init_opt(p):
    '''init_opt :
       | ASSIGNMENT expression
    '''
    if (Debug1) : print "Rule Declared: 12"
    if (len(p) == 3):
        p[0] = p[2]
    else:
        p[0] = None

def p_number_decl(p):
    '''number_decl : def_id_s ':' CONSTANT ASSIGNMENT expression ';'
    '''
    if (len(p[1])  == 0) :
        print "[Number Declaration] Error : No objects to declare"
        p_error(p)
    
    else:

        for item in p[1]:
            item_lexeme = item
            item = item.lower()
            flag = True

            if item in reserved :
                flag = False
                print "[Number Declaration] Error : Object " + item + " is a reserved keyword"
                p_error(p)

            if symbol_table.locate_Symbol_in_this(item):
                flag = False
                print "[Number Declaration] Error : Object " + item + " has been already defined in this scope"
                p_error(p)
              
            if flag :
                symbol_table.createSym(item , {'isarray': False, 'lexeme': item_lexeme, 'type': p[5]["type"], 'value': None, 'offset':  symbol_table.get_width() , "isconstant" : True}) # I will ensure that p[4] is a dictionary having type information
                symbol_table.change_width(get_type_width(p[5])) #Has been set up while evaluating for p[4]
                three_addr_code.emit(item_lexeme , p[5]["value"] , ":=" , None)

    if (Debug1) : print "Rule Declared: 13"

def p_type_decl(p):
    '''type_decl : TYPE IDENTIFIER discrim_part_opt type_completion ';'
    '''
    if (Debug1) : print "Rule Declared: 14"

    if (symbol_table.locate_Symbol_in_this(p[2])):
        print "[Type Declaration] Error : Type " + p[2] + " has been already defined in this scope"
        p_error(p)

    elif p[2] in reserved : 
        print "[Type Declaration] Error : Name " + item + " is a reserved keyword" 
        p_error(p)
    else:
        temp = deepcopy(p[4])
        temp.update({"istype" : True , "lexeme" : p[2] , "type" : p[2].lower() })
        symbol_table.createSym(p[2]  , temp)
        p[0] = symbol_table.get_row(p[2])

        ##################################################################################################

def p_discrim_part_opt(p):
    '''discrim_part_opt :
       | discrim_part
       | '(' LESSMORE ')'
    '''
    if (Debug1) : print "Rule Declared: 15"

def p_type_completion(p):
    '''type_completion :
       | IS type_def
    '''
    if(len(p) == 1):
        p[0] = {"type" : None}
    else:
        p[0] = deepcopy(p[2])

    if (Debug1) : print "Rule Declared: 16"

def p_type_def(p):
    '''type_def : enumeration_type 
       | integer_type
       | real_type
       | array_type
       | record_type
       | access_type
       | derived_type
       | private_type
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 17"


def p_subtype_decl(p):
    '''subtype_decl : SUBTYPE IDENTIFIER IS subtype_ind ';'
    '''
    if (symbol_table.locate_Symbol_in_this(p[2])):
        print "[Type Declaration] Error : Type " + p[2] + " has been already defined in this scope"
        p_error(p)

    elif p[2] in reserved : 
        print "[Type Declaration] Error : Name " + item + " is a reserved keyword" 
        p_error(p)

    else:
        print "got a sub-type"

        attributes = deepcopy(p[4])
        attributes.update({"istype" : True , "lexeme" : p[2] , "type" : p[2].lower()})
        symbol_table.createSym(p[2] , attributes)
        p[0] = symbol_table.get_row(p[2])

    if (Debug1) : print "Rule Declared: 18"

#A list needs to be carried forwards
def p_subtype_ind(p):
    '''subtype_ind : name constraint
       | name
    '''
    p[0] = {}

    if ( symbol_table.locate_Symbol(p[1]["lexeme"]) and (symbol_table.get_Attribute_Value(p[1]["lexeme"] , "istype") != None) and (symbol_table.get_Attribute_Value(p[1]["lexeme"] , "istype"))):
        if(len(p) == 3):
            p[0].update(p[2]) #p[2] is a dictionary , Tranferring constraints

        p[0] = deepcopy(p[1])
        if("isarray" not in p[1]):
            p[0].update({"isarray" : False})    
        p[0].update({"istype":False, "lexeme" : None})      

    else:
        print "[Inconsistent Type] Error at line " , " : Type does not exists"
        p_error(p)

    if (Debug1) : print "Rule Declared: 19"


def p_constraint(p):
    '''constraint : range_constraint
       | decimal_digits_constraint
    '''
    if (Debug1) : print "Rule Declared: 20"
    p[0] = p[1]

#*********************** REMOVE IT LATER ON *******************
def p_decimal_digits_constraint(p):
    '''decimal_digits_constraint : DIGITS expression range_constr_opt
    '''
    if (Debug1) : print "Rule Declared: 21"

def p_derived_type(p):
    '''derived_type : NEW subtype_ind
       | NEW subtype_ind WITH PRIVATE
       | NEW subtype_ind WITH record_def
       | ABSTRACT NEW subtype_ind WITH PRIVATE
       | ABSTRACT NEW subtype_ind WITH record_def
    '''
    if (Debug1) : print "Rule Declared: 22"


def p_range_constraint(p):
    '''range_constraint : RANGE range
    '''
    if (Debug1) : print "Rule Declared: 23"
    p[0] = p[2]


def p_range(p):
    '''range : simple_expression DOTDOT simple_expression
        | name
    '''
    if(len(p) == 4):
        if (p[1]["type"] != p[3]["type"]) :
            print "[Range Declaration] Error at " , ": Range start and End type do not match"
            p_error(p)
        else:
            p[0] = {"lower_limit" : p[1]["value"], "upper_limit" : p[3]["value"] , "index_bound_type" : p[1]["type"] }
    
    else:

        p[0] = None

        if (symbol_table.locate_Symbol(p[1]["lexeme"])):
            if("upper_limit" in p[1] and "lower_limit" in p[1] and p[1]["upper_limit"] != None and p[1]["lower_limit"]!= None):
                #Range Type
                p[0] = deepcopy(p[1])
        else:
            print "[Range] Error at line",p.lineno(1),": Range not declared before"
            p_error(p)
            
    if (Debug1) : print "Rule Declared: 24"


def p_enumeration_type(p):
    '''enumeration_type : '(' enum_id_s ')'
    '''
    p[0] = p[2]
    if (Debug1) : print "Rule Declared: 25"

def p_enum_id_s(p):
    '''enum_id_s : enum_id
       | enum_id_s ',' enum_id
    '''
    if (Debug1) : print "Rule Declared: 26"


def p_enum_id(p):
    '''enum_id : IDENTIFIER
       | CHAR
    '''
    if (Debug1) : print "Rule Declared: 27"


def p_integer_type(p):
    '''integer_type : range_spec
    '''
    if(len(p) == 2):
        p[0] = deepcopy(p[1])

    if (Debug1) : print "Rule Declared: 28"


def p_range_spec(p):
    '''range_spec : range_constraint
    '''
    p[0] = p[1]
    if (Debug1) : print "Rule Declared: 30"

def p_range_spec_opt(p):
    '''range_spec_opt :
       | range_spec
    '''
    if(len(p) == 1):
        p[0] = None
    else:
        p[0] = p[1]
    if (Debug1) : print "Rule Declared: 31"


#++++++++++++++Later On+++++++++++++++++++++
def p_real_type(p):
    '''real_type : float_type
       | fixed_type
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 32"


def p_float_type(p):
    '''float_type : DIGITS expression range_spec_opt
    '''
    if (Debug1) : print "Rule Declared: 33"

#++++++++++++++++++++ Later On ++++++++++++++++++++

def p_fixed_type(p):
    '''fixed_type : DELTA expression range_spec
       | DELTA expression DIGITS expression range_spec_opt
    '''
    if (Debug1) : print "Rule Declared: 34"


def p_array_type(p):
    '''array_type : unconstr_array_type
       | constr_array_type
    '''
    p[0] = p[1]
    if (Debug1) : print "Rule Declared: 35"


#************* REMOVE LATER ***********************************************************************

def p_unconstr_array_type(p):
    '''unconstr_array_type : ARRAY '(' index_s ')' OF component_subtype_def
    '''
    if (Debug1) : print "Rule Declared: 36"

#************* REMOVE LATER ***********************************************************************


#Handled multi dimentional arrays as well
def p_constr_array_type(p):
    '''constr_array_type : ARRAY iter_index_constraint OF subtype_ind
    '''
    numvalues = 1
    p[0] = deepcopy(p[4])
    p[0] = {"lower_limit" : [] , "upper_limit" : [] , "indextype" : []  , "isarray" : True}

    #Useful for multi-dimentional arrays
    for item in p[2]:
        p[0]["lower_limit"].append(item["lower_limit"])
        p[0]["upper_limit"].append(item["upper_limit"])
        p[0]["indextype"].append(item["index_bound_type"])
        numvalues = numvalues*(item["upper_limit"] - item["lower_limit"] + 1)

    type_size = numvalues * get_type_width(p[4])
    p[0].update({"numvalues" : numvalues , "base_type" : p[4]["type"]  , "type" : p[4]["type"] , "offset" : symbol_table.get_width() , "width":type_size})

    symbol_table.change_width(type_size)

    if (Debug1) : print "Rule Declared: 37"


def p_component_subtype_def(p):
    '''component_subtype_def : aliased_opt subtype_ind
    '''
    if (Debug1) : print "Rule Declared: 38"


def p_aliased_opt(p):
    '''aliased_opt : 
       | ALIASED
    '''
    if (Debug1) : print "Rule Declared: 39"


def p_index_s(p):
    '''index_s : index
       | index_s ',' index
    '''
    if (Debug1) : print "Rule Declared: 40"


def p_index(p):
    '''index : name RANGE LESSMORE
    '''
    if (Debug1) : print "Rule Declared: 41"


def p_iter_index_constraint(p):
    '''iter_index_constraint : '(' iter_discrete_range_s ')'
    '''
    p[0] = deepcopy(p[2])
    if (Debug1) : print "Rule Declared: 42"


def p_iter_discrete_range_s(p):
    '''iter_discrete_range_s : discrete_range
       | iter_discrete_range_s ',' discrete_range
    '''
    if(len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
    if (Debug1) : print "Rule Declared: 43"


#*************** To be corrected ****************
def p_discrete_range(p):
    '''discrete_range : name range_constr_opt
       | range
    '''

    if(len(p) == 2):
        p[0] = p[1]
    else:
        return None
    if (Debug1) : print "Rule Declared: 44"


def p_range_constr_opt(p):
    '''range_constr_opt :
       | range_constraint
    '''
    if (Debug1) : print "Rule Declared: 45"


def p_record_type(p):
    '''record_type : tagged_opt limited_opt record_def
    '''
    if (Debug1) : print "Rule Declared: 46"


def p_record_def(p):
    '''record_def : RECORD pragma_s comp_list END RECORD
       | NuLL RECORD
    '''
    if (Debug1) : print "Rule Declared: 47"


def p_tagged_opt(p):
    '''tagged_opt :
       | TAGGED
       | ABSTRACT TAGGED
    '''
    if (Debug1) : print "Rule Declared: 48"


def p_comp_list(p):
    '''comp_list : comp_decl_s variant_part_opt
       | variant_part pragma_s
       | NuLL ';' pragma_s
    '''
    if (Debug1) : print "Rule Declared: 49"


def p_comp_decl_s(p):
    '''comp_decl_s : comp_decl
       | comp_decl_s pragma_s comp_decl
    '''
    if (Debug1) : print "Rule Declared: 50"


def p_variant_part_opt(p):
    '''variant_part_opt : pragma_s
       | pragma_s variant_part pragma_s
    '''
    if (Debug1) : print "Rule Declared: 51"


def p_comp_decl(p):
    '''comp_decl : def_id_s ':' component_subtype_def init_opt ';'
       | error ';'
    '''
    if (Debug1) : print "Rule Declared: 52"


def p_discrim_part(p):
    '''discrim_part : '(' discrim_spec_s ')'
    '''
    if (Debug1) : print "Rule Declared: 53"


def p_discrim_spec_s(p):
    '''discrim_spec_s : discrim_spec
       | discrim_spec_s ';' discrim_spec
    '''
    if (Debug1) : print "Rule Declared: 54"


def p_discrim_spec(p):
    '''discrim_spec : def_id_s ':' access_opt mark init_opt
       | error
    '''
    if (Debug1) : print "Rule Declared: 55"


def p_access_opt(p):
    '''access_opt :
       | ACCESS
    '''
    if (Debug1) : print "Rule Declared: 56"


def p_variant_part(p):
    '''variant_part : CASE simple_name IS pragma_s variant_s END CASE ';'
    '''
    if (Debug1) : print "Rule Declared: 57"


def p_variant_s(p):
    '''variant_s : variant
       | variant_s variant
    '''
    if (Debug1) : print "Rule Declared: 58"


def p_variant(p):
    '''variant : WHEN choice_s ARROW pragma_s comp_list
    '''
    if (Debug1) : print "Rule Declared: 59"


def p_choice_s(p):
    '''choice_s : choice
       | choice_s '|' choice
    '''
    if (Debug1) : print "Rule Declared: 60"


def p_choice(p):
    '''choice : expression
       | discrete_with_range
       | OTHERS
    '''
    if (Debug1) : print "Rule Declared: 61"


def p_discrete_with_range(p):
    '''discrete_with_range : name range_constraint
       | range
    '''
    if (Debug1) : print "Rule Declared: 62"


def p_access_type(p):
    '''access_type : ACCESS subtype_ind
       | ACCESS CONSTANT subtype_ind
       | ACCESS ALL subtype_ind
       | ACCESS prot_opt PROCEDURE formal_part_opt
       | ACCESS prot_opt FUNCTION formal_part_opt RETURN mark
    '''
    if (Debug1) : print "Rule Declared: 63"


def p_prot_opt(p):
    '''prot_opt :
       | PROTECTED
    '''
    if (Debug1) : print "Rule Declared: 64"


def p_decl_part(p):
    '''decl_part :
       | decl_item_or_body_s1
    '''
    if (len(p) == 1):
        p[0] = None
    else:
        p[0] = p[1]

    if (Debug1) : print "Rule Declared: 65"


def p_decl_item_s(p):
    '''decl_item_s : 
       | decl_item_s1
    '''
    if (Debug1) : print "Rule Declared: 66"


def p_decl_item_s1(p):
    '''decl_item_s1 : decl_item
       | decl_item_s1 decl_item
    '''
    if (Debug1) : print "Rule Declared: 67"


def p_decl_item(p):
    '''decl_item : decl
       | use_clause
       | rep_spec
       | pragma
    '''
    p[0] =p[1]
    if (Debug1) : print "Rule Declared: 68"


def p_decl_item_or_body_s(p):
    '''decl_item_or_body_s1 : decl_item_or_body
       | decl_item_or_body_s1 decl_item_or_body
    '''
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

    if (Debug1) : print "Rule Declared: 69"


def p_decl_item_or_body(p):
    '''decl_item_or_body : body
       | decl_item
    '''
    p[0] = p[1]

    if (Debug1) : print "Rule Declared: 70"


def p_body(p):
    '''body : subprog_body
       | pkg_body
       | task_body
       | prot_body
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 71"


def p_name(p):
    '''name : simple_name
       | indexed_comp
       | selected_comp
       | attribute
       | operator_symbol
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 72"


def p_mark(p):
    '''mark : simple_name
       | mark TICK attribute_id
       | mark '.' simple_name
    '''
    if(len(p) == 2): p[0] = deepcopy(p[1])
    else:
        p[0] = None 
        print " Not Handled yet"

    if (Debug1) : print "Rule Declared: 73"


#This identifier has to be declared before
def p_simple_name(p):
    '''simple_name : IDENTIFIER
    '''
    symbol_table.updateSym(p[1] , "value" , p[1])

    if( symbol_table.locate_Symbol(p[1].lower()) ):
        #print p[1].lower()
        #print symbol_table.get_row(p[1].lower())
        p[0] = symbol_table.get_row(p[1].lower()) #I get a dictionary here

    else:
        p[0] = {"lexeme" : p[1] , "value" : p[1] , "type": p[1]} #For variables used in labels, procedure calls , etc
        if(p[1] == "true"):
            p[0].update({"type":"BOOL" , "value":1})
        if(p[1] == "false"):
            p[0].update({"type":"BOOL" , "value":0})
    if (Debug1) : print "Rule Declared: 74"
    

def p_compound_name(p):
    '''compound_name : simple_name
       | compound_name '.' simple_name
    '''
    if(len(p) == 2):
        p[0] = deepcopy(p[1])

    else:
        p[0] = None
        print "not handled yet"

    if (Debug1) : print "Rule Declared: 75"


def p_c_name_list(p):
    '''c_name_list : compound_name
        | c_name_list ',' compound_name
    '''
    if (Debug1) : print "Rule Declared: 76"


def p_used_char(p):
    '''used_char : CHAR
    '''
    p[0] = {"value" : p[1], "type" : "CHAR" , "lexeme" : p[1] , "isbase" : False}
    if (Debug1) : print "Rule Declared: 77"



def p_operator_symbol(p):
    '''operator_symbol : STRING
    '''
    if (Debug1) : print "Rule Declared: 78"


#Matches a lot of things , Need to handle them here
def p_indexed_comp(p):
    '''indexed_comp : name '(' value_s ')'
    '''
    # I am getting a list of values here

    p[0] = deepcopy(p[1])

    if(symbol_table.locate_Symbol(p[1]["lexeme"])):

        #Not handled pre-assigned values yet
        #Procedure Call
        if(symbol_table.get_Attribute_Value(p[1]["lexeme"] , "isprocedure") != None and symbol_table.get_Attribute_Value(p[1]["lexeme"] , "isprocedure")):
            if(len(p[3]) != len(symbol_table.get_Attribute_Value(p[1]["lexeme"] , "var_List"))) :
                print "[Procedure Call] Error : Number of Arguments passed do not agree with procedures"
                p_error(p)
            else:
                parameter_list = symbol_table.get_Attribute_Value(p[1]["lexeme"] , "var_List")
                flag = True
                count = 0 

                for item in p[3]:
                    if(item["type"] != parameter_list[count]["dictionary"]["type"]):
                        flag = False
                    count += 1

                if not flag :
                    print "[Procedure Call] Error : Argument Types do not match"
                    p_error(p)

                else:
                    i = 0
                    in_count = 0 

                    for item in parameter_list:
                        if(item["dictionary"]["paramtype"] == "in"):
                            in_count += 1 

                    while i <= len(p[3])  - 1:
                        if in_count > 0 :
                            three_addr_code.emit('parameter',(p[3][i])['lexeme'],None,None);
                            in_count = in_count  - 1
                        else:
                            three_addr_code.emit('parameter',(p[3][i])['lexeme'],'out',None);
                        i=i+1

                    three_addr_code.emit("procedure_call" , p[1]["lexeme"] , len(p[3]) , None)

        elif (symbol_table.get_Attribute_Value(p[1]["lexeme"] , "isarray") != None and symbol_table.get_Attribute_Value(p[1]["lexeme"] , "isarray")):
        
        #Allow out of bounds access
            if(len(p[3]) != len(symbol_table.get_Attribute_Value(p[1]["lexeme"] , "upper_limit"))):
                print "[Array Access] Error : Wrong number of dimensions requested"
                p_error(p)

            else:
                i  = 0 ; 
                flag = True; 

                for item in p[3]:
                    if not (item["type"] == p[1]["indextype"][i]):
                        flag = False
                        
                    i = i + 1; 

                if(flag):
                    loop_temp = None

                    for i in range(0, len(p[3]) - 1):
                        new_temp1 = get_temp("INT")
                        new_temp2 = get_temp("INT")
    
                        three_addr_code.emit(new_temp1 , p[3][i]["value"] , '-' , p[1]["lower_limit"][i] )
                        three_addr_code.emit(new_temp2 , p[1]["upper_limit"][i] - p[1]["lower_limit"][i] + 1 , '*' , new_temp1)
                    
                        if(loop_temp != None):
                                new_temp3 = get_temp("INT")
                                three_addr_code.emit(new_temp3 , new_temp2 , '+' , loop_temp)
                                loop_temp = new_temp3
                        else:
                                loop_temp =new_temp2 

                    offset_temp = None
                    new_temp5 = get_temp("INT")
                    three_addr_code.emit(new_temp5 , p[3][len(p[3]) - 1]["value"] , '-' , p[1]["lower_limit"][len(p[3]) - 1] ) 
                    if(loop_temp == None):
                        offset_temp = new_temp5
                    else:
                        offset_temp = get_temp("INT")
                        three_addr_code.emit(offset_temp , loop_temp ,  '+'  , new_temp5)


                    offset_value = get_temp("INT")
                    three_addr_code.emit(offset_value , get_type_width(p[1]["base_type"]), '*' , offset_temp)
                    
                        #compute some values here.. 
                    p[0]["value"] = p[1]["lexeme"] + '(' + offset_value + ')'
                    p[0]["lexeme"] = p[1]["lexeme"] + '(' + offset_value + ')'
                    p[0]["type"] = p[1]["base_type"]
                else:
                    print "[Type Mismatch] Error at line",p.lineno(2),": arguments types do not match to the index types of the array",p[1]["lexeme"]
                    p_error(p)
                #correct it here

    else :
        print "[Calling] Error : " + p[1]["lexeme"] + " has not been declared yet. Unable to Handle this"
        p_error(p)

    if (Debug1) : print "Rule Declared: 79"


def p_value_s(p):
    '''value_s : value
       | value_s ',' value
    '''
    if (len(p) == 2): p[0] = [p[1]]
    else : 
        p[0] = p[1] + [p[3]]

    if (Debug1) : print "Rule Declared: 80"


def p_value(p):
    '''value : expression
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 81"


def p_value3(p):
    '''value : comp_assoc
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 81"

def p_value1(p):
    '''value : error
    '''
    p[0] = []
    print "[Argument] Error at line :",p.lineno(1),"Argument passing error"
    p_error(p)

def p_selected_comp(p):
    '''selected_comp : name '.' simple_name
       | name '.' used_char
       | name '.' operator_symbol
       | name '.' ALL
    '''
    if (Debug1) : print "Rule Declared: 82"


def p_attribute(p):
    '''attribute : name TICK attribute_id
    '''
    if (Debug1) : print "Rule Declared: 83"


def p_attribute_id(p):
    '''attribute_id : IDENTIFIER
       | DIGITS
       | DELTA
       | ACCESS
    '''
    if (Debug1) : print "Rule Declared: 84"


def p_literal1(p):
    '''literal : INTEGER
    '''
    if (Debug1) : print "Rule Declared: 85"
    p[0] = {"value" : p[1] , "type" : "INT" , "isbase" : False}

def p_literal2(p):
    '''literal : BASE_INTEGER
    '''
    if (Debug1) : print "Rule Declared: 85"
    p[0] = {"value" : p[1] , "type" : "INT" , "isbase" : True}

def p_literal3(p):
    '''literal : FLOAT
    '''
    if (Debug1) : print "Rule Declared: 85"
    p[0] = {"value" : p[1] , "type" : "FLOAT" , "isbase" : False}

def p_literal4(p):
    '''literal : BASE_FLOAT
    '''
    if (Debug1) : print "Rule Declared: 85"
    p[0] = {"value" : p[1] , "type" : "FLOAT" , "isbase" : True}

def p_literal5(p):
    '''literal : used_char
    '''
    if (Debug1) : print "Rule Declared: 85"
    p[0] = p[1]

def p_literal6(p):
    '''literal : NuLL
    '''
    if (Debug1) : print "Rule Declared: 85"
    p[0] = p[1]

def p_aggregate (p) : 
    ''' aggregate :   '(' comp_assoc ')'
        | '(' value_s_2 ')'
        | '(' expression WITH value_s ')'
        | '(' expression WITH NuLL RECORD ')'
        | '(' NuLL RECORD ')'
    '''
    
    if (Debug1): print "Rule Declared: 87"

def p_value_s_(p):
    '''value_s_2 : value ',' value
       | value_s_2 ',' value
    '''
    if (Debug1) : print "Rule Declared: 87"


def p_comp_assoc(p):
    '''comp_assoc : choice_s ARROW expression
    '''

    if (Debug1) : print "Rule Declared: 88"

def p_m(p):
    '''m :
    '''
    p[0] = {"quad" : three_addr_code.get_next_instr_no()}

def p_expression1(p):
    '''expression : relation
       | expression logical  m relation
    '''
    if(len(p) == 2):
        if (Debug2) : print "relation"
        p[0] = p[1]

    else: #Non-Short-Circuited Expressions
        if (p[1]["type"] != "BOOL") or (p[4]["type"] != "BOOL") :
            print "[Type Mismatch] Error : Non-Boolean expressions used as Booleans"
            p_error(p)

        else:
            p[0] = deepcopy(p[4]) #Carrying other attributes, like type , etc
    
            if (p[2] == "and") :
                backpatch(p[1]["truelist"] , p[3]["quad"])
                p[0]["falselist"]  = merge(p[1]["falselist"] , p[4]["falselist"])
                p[0]["truelist"] = p[4]["truelist"]
                temp = get_temp(p[1]["type"])
                three_addr_code.emit(temp , p[1]["value"] , 'and' , p[4]["value"])

            else : #"or" case
                backpatch(p[1]["falselist"] , p[3]["quad"])
                p[0]["truelist"]  = merge(p[1]["truelist"] , p[4]["truelist"])
                p[0]["falselist"] = p[4]["falselist"]
                temp = get_temp(p[1]["type"])
                three_addr_code.emit(temp , p[1]["value"] , 'or' , p[4]["value"])

            #Temp variables are created in case, it is an expression when goto statements are removed
            p[0]["value"] = temp    #***************************************** SHOULD IT BE DONE  ?

    if (Debug1) : print "Rule Declared: 89"


#*********** THERE SHOULD BE SOME EMIT HERE *************************
def p_expression2(p):
    '''expression : expression short_circuit m relation
    '''
    if (p[1]["type"] != "BOOL") or (p[4]["type"] != "BOOL") :
            print "[Type Mismatch] Error : Non-Boolean expressions used as Booleans"
            p_error(p)


    p[0] = deepcopy(p[1]) #the value of p[1] has been copied


    if (p[2] == "and"):
        backpatch(p[1]['truelist'],p[3]['quad'])
        p[0]['falselist']=merge(p[1]['falselist'],p[4]['falselist'])
        p[0]['truelist']=p[4]['truelist']

    else:
        backpatch(p[1]['falselist'],p[3]['quad'])
        p[0]['truelist']=merge(p[1]['truelist'],p[4]['truelist'])
        p[0]['falselist']=p[4]['falselist']

        #Value need not be saved here
    if (Debug1) : print "Rule Declared: 89"

def p_logical(p):
    '''logical : AND
       | OR
    '''
    p[0] = p[1] #I will ignore XOR later on
    if (Debug1) : print "Rule Declared: 90"

def p_short_circuit(p):
    '''short_circuit : AND THEN
       | OR ELSE
    '''

    p[0] = p[1] #Returns whether it is 'or' or 'and' 

    if (Debug1) : print "Rule Declared: 91"


def p_relation1(p):
    '''relation : simple_expression
       | simple_expression relational simple_expression
    '''
    if(len(p) == 2):
        p[0] = deepcopy(p[1])
        if (Debug2) : "expression Received : " + str(p[1])

    else :
        if(Debug2) : print "Some Computation Done"
        if (p[1]["type"] != p[3]["type"]):
            print "[Type Inconsistent] Error : relation on different Types"
            p_error(p)
            p[0] = {"type" : None , "value" : None , "lexeme" : None}
        else:
            p[0] = deepcopy(p[1])
            p[0]["type"] = "BOOL"

            if(p[1]["type"] == "INT"):
                operator = 'int_' + p[2]
            elif (p[1]["type"] == "FLOAT"):
                operator = 'float_' + p[2]
            else:
                operator = p[2]

            temp = get_temp(p[0]["type"])
            three_addr_code.emit(temp , p[1]["value"] , operator , p[3]["value"] )
            p[0]["value"] = temp

            #May not be always used
            p[0]['truelist'] = makeList(three_addr_code.get_next_instr_no())
            p[0]['falselist'] = makeList(three_addr_code.get_next_instr_no()+1)
        
            three_addr_code.emit("goto", temp , None ,  None)
            three_addr_code.emit('goto', None , None , None)



    if (Debug1) : print "Rule Declared: 92"


#*********************HANDLE LATER **********************
def p_relation2(p):
    '''relation : simple_expression membership range
       | simple_expression membership name
    '''

    if (Debug1) : print "Rule Declared: 92"


#********************* ALl DOne after**********************************

def p_relational(p):
    '''relational : '='
       | NOTEQUAL
       | '<'
       | LESSEQ
       | '>'
       | GREATEREQ
    '''
    p[0] = p[1]
    if (Debug1) : print "Rule Declared: 93"

def p_membership(p):
    '''membership : IN
       | NOT IN
    '''
    if(len(p) == 1) : p[0] = "in"
    else : p[0] = "notin"
    if (Debug1) : print "Rule Declared: 94"

def p_simple_expression(p):
    '''simple_expression : unary term
       | term
       | simple_expression adding term
    '''

    p[0] = {"value" : None , "type" : "Statement"}

    if(len(p) == 2):
        p[0] = deepcopy(p[1])

    elif(len(p) == 3): 
        #Checking Type compatiablity
        if not (p[2]["type"] == "INT" or p[2]["type"] == "FLOAT"):
            print "[Expression Computations] Error at line " , " : unary operator used on a wrong subtype"
            p_error(p)

        temp = get_temp(p[2]["type"])

        p[0] = deepcopy(p[2])

        rhs = p[2]["value"]
        #SDD's are constraints not computations
        if("lexeme" in p[2] and p[2]["lexeme"] != None):
            rhs = p[2]["lexeme"]

        if(p[2]["type"] == "INT"):
            if(p[1] == '-'):
                three_addr_code.emit(temp, None , "int_un-" , rhs)
            else:
                three_addr_code.emit(temp , None , "int_un+" , rhs)
        else:
            if(p[1] == '-'):
                three_addr_code.emit(temp, None , "float_un-" , rhs)
            else:
                three_addr_code.emit(temp , None , "float_un+" , rhs)           


        p[0]["value"] = temp #Values of both the variables are same
        #p[0]["lexeme"] = temp



    else:
        if not ((p[1]["type"] == "INT" or p[1]["type"] == "FLOAT") and (p[3]["type"] == "INT" or p[3]["type"] == "FLOAT")):
            print "[Expression Computations] Error at line " , " : Binary operator used on a wrong subtype"
            p_error(p)

        elif (p[1]["type"] != p[3]["type"]):
            print "[Expression Computations] Error at line " , " : operand types do not match"
            p_error(p)

        else:
            if(p[1]["type"] == "INT"):
                operator = 'int_' + p[2] 
            elif(p[1]["type"] == "FLOAT"):
                operator = 'float_' + p[2]
            else:
                operator = p[2]

            temp = get_temp(p[1]["type"])
            p[0] = deepcopy(p[1]) #Copying Other Attributes
            operand1 = p[1]["value"]
            operand2 = p[3]["value"]
            if("lexeme" in p[1] and symbol_table.locate_Symbol(p[1]["lexeme"])):
                operand1  = p[1]["lexeme"]

            if("lexeme" in p[3] and symbol_table.locate_Symbol(p[3]["lexeme"])):
                operand2  = p[3]["lexeme"]

            three_addr_code.emit(temp , operand1 , operator , operand2)

            p[0]["value"] = temp #Values of both the variables are same
            p[0]["lexeme"] = temp

    if (Debug1) : print "Rule Declared: 95"

def p_unary(p):
    '''unary   : '+'
       | '-'
    '''
    p[0] = p[1]
    if (Debug1) : print "Rule Declared: 96"

def p_adding(p):
    '''adding  : '+'
       | '-'
       | '&'
    '''
    p[0] = p[1]
    if (Debug1) : print "Rule Declared: 97"

def p_term(p):
    '''term    : factor
       | term multiplying factor
    '''
    if (len(p) == 2):
        p[0] = p[1]

    else:
        if not ((p[1]["type"] == "INT" or p[1]["type"] == "FLOAT") and (p[3]["type"] == "INT" or p[3]["type"] == "FLOAT")):
            print "[Expression Computations] Error at line " , " : Binary operator used on a wrong subtype"
            p_error(p)

        elif (p[1]["type"] != p[3]["type"]):
            print "[Expression Computations] Error at line " , " : operand types do not match"
            p_error(p)

        else:
            temp = get_temp(p[1]["type"])
            p[0] = deepcopy(p[1]) #Copying Other Attributes
            three_addr_code.emit(temp , p[1]["value"] , p[2] , p[3]["value"])
            p[0]["value"] = temp #Values of both the variables are same


    if (Debug1) : print "Rule Declared: 98"

#Numerical Operators only
def p_multiplying(p):
    '''multiplying : '*'
       | '/'
       | MOD
       | REM
    '''
    p[0]= p[1]
    if (Debug1) : print "Rule Declared: 99"

def p_factor(p):
    '''factor : primary
       | NOT primary
       | primary STARSTAR primary
    '''
    if (len(p) == 2):
        p[0] = p[1]

    elif (len(p) == 3): #For booleans Only

        if(p[2]["type"] != "BOOL"):
            print "[Expression Computations] Error at line " , " : opeand should be of BOOL type"
            p_error(p)
        else:
            p[0] = p[2]

            if(p[2]["value"] == True):
                p[0]["value"] = False
            else:
                p[0]["value"] = False

            p[0]['truelist']=p[2]['falselist']
            p[0]['falselist']=p[0]['truelist']

    else:
        if not ((p[1]["type"] == "INT" or p[1]["type"] == "FLOAT") and (p[3]["type"] == "INT" or p[3]["type"] == "FLOAT")):
            print "[Expression Computations] Error at line " , " : Binary operator used on a wrong subtype"
            p_error(p)

        elif (p[1]["type"] != p[3]["type"]):
            print "[Expression Computations] Error at line " , " : operand types do not match"
            p_error(p)

        p[0]=deepcopy(p[1])
        temp=get_temp(p[1]["type"])
        three_addr_code.emit(temp ,p[1]["value"],"dotdot" , p[3]["value"])
        p[0]['value']=temp


    if (Debug1) : print "Rule Declared: 100"

def p_primary(p):
    '''primary : literal
       | name
       | allocator
       | qualified
       | parenthesized_primary
    '''
    p[0]  = p[1]
    if (Debug1) : print "Rule Declared: 101"

def p_parenthesized_primary (p) : 
    '''parenthesized_primary :   aggregate
        | '(' expression ')'
    '''
    if(len(p) >2):
        p[0] = p[2]

#****************TO BE REMOVED**************************
def p_qualified (p) : 
    '''qualified :   name TICK parenthesized_primary
    '''


def p_allocator(p):
    '''allocator : NEW name
       | NEW qualified
    '''
    if (Debug1) : print "Rule Declared: 104"
#*********************************************************

def p_statement_s(p):
    '''statement_s : statement
       | statement_s m statement
    ''' #m has been defined before

    if(Debug2) : "Defining statement"
    p[0] = deepcopy(p[1])

    if(len(p) == 4) :
        if (p[3] != None):
            p[0] = deepcopy(p[3])
            backpatch(p[1]["nextlist"],p[2]["quad"])
            p[0]["nextlist"] = p[3]["nextlist"]
            if(Debug2) : print "adding " + str(p[3]) + " to Statement List"
        else:
            print "[Statement Type] Error : Statement format not found/defined in the language grammar"  

    if (Debug1) : print "Rule Declared: 105"


#*************************** LAbelling Still left , Allow labelled Statements 

def p_statement(p):
    '''statement : unlabeled
       | label statement
    '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = p[2]
    if (Debug1) : print "Rule Declared: 106"


def p_unlabeled(p):
    '''unlabeled : simple_stmt
       | compound_stmt
       | pragma
    '''
    p[0] = p[1]
    if (Debug1) : print "Rule Declared: 107"


#Handle Errors Seperately
def p_simple_stmt(p):
    '''simple_stmt : null_stmt
       | assign_stmt
       | exit_stmt
       | return_stmt
       | goto_stmt
       | procedure_call
       | delay_stmt
       | abort_stmt
       | raise_stmt
       | code_stmt
       | requeue_stmt
       | error ';'
    '''
    if(len(p) == 3):
        print "[Statement] Error at line " + str(p.lineno(1)) + " : Not a valid statement"
        p_error(p)

    else:
        p[0] = p[1]
    if not (not p[0] == None and "nextlist" in p[0]):
        p[0] ={"nextlist" : []}
    if (Debug1) : print "Rule Declared: 108"

def p_compound_stmt(p):
    '''compound_stmt : if_stmt
       | case_stmt
       | loop_stmt
       | block
       | accept_stmt
       | select_stmt
    '''
    p[0] ={"nextlist" : []}
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 109"

#******************************************************
def p_label(p):
    '''label : LESSLESS IDENTIFIER MOREMORE
    '''
    if (Debug1) : print "Rule Declared: 110"


def p_null_stmt(p):
    '''null_stmt : NuLL ';'
    '''
    p[0] = {"nextlist" : []}
    if (Debug1) : print "Rule Declared: 111"

#I am not allowing a casting from BOOL to int types
def p_assign_stmt(p):
    '''assign_stmt : name ASSIGNMENT expression ';'
    '''
    #All variables are pre-defined
    name = p[1]["lexeme"]

    if not (p[1]["isarray"]) and not symbol_table.locate_Symbol(name) :
        print "[Illegal Assignment] Error at line " + str(p.lineno(2)) + " : Variable " +  name + " not declared"
        p_error(p)

    else:

        istype = symbol_table.get_Attribute_Value(name , "istype")
        isconstant = symbol_table.get_Attribute_Value(name , "isconstant")
        
        if isconstant != None and isconstant :
            print "[Illegal Assignment] Error at line " + str(p.lineno(2)) + " : Variable " +  name + " is a constant varaible and can not be reassigned"
            p_error(p)

        if  istype != None and istype:
            print "[Illegal Assignment] Error at line " + str(p.lineno(2)) + " : Variable " +  name + " is a type"
            p_error(p)  

        if (p[1]["type"] == p[3]["type"]) : #Legal Assignment

            p[0]  = deepcopy(p[3])
            p[0]["nextlist"] = [] #empty_list

            three_addr_code.emit(p[1]["lexeme"] , p[3]["value"] , ":=" , None) #Emitting this assignment
            p[0]["type"] = "Statement"

        else:
            print "[Illegal Assignment] Error at line " + str(p.lineno(2)) + " : Variable " +  name + " does not have the same type as RHS"
            p_error(p)
            
    print "assignment done"
    if (Debug1) : print "Rule Declared: 112"

def p_if_stmt(p):
    '''if_stmt : IF cond_clause_s else_opt END IF ';'
    '''
    p[0] = deepcopy(p[2])
    p[0]["nextlist"] = merge(p[2]["nextlist"] , p[3]["nextlist"])
    backpatch(p[2]["falselist"] , p[3]["quad"])

    if (Debug1) : print "Rule Declared: 113"

def p_cond_clause_s(p):
    '''cond_clause_s : cond_clause
       | cond_clause ELSIF m cond_clause_s
    '''

    p[0] = deepcopy(p[1])   

    if(len(p) > 2): 
        p[0]["nextlist"] = merge(p[1]["nextlist"] , p[4]["nextlist"])
        backpatch(p[1]["falselist"] , p[3]["quad"])
        p[0]["falselist"] = p[4]["falselist"]

    if (Debug1) : print "Rule Declared: 114"

def p_n(p):
    ''' n :
    '''
    p[0] = {"nextlist" : [three_addr_code.get_next_instr_no()]}
    three_addr_code.emit("goto" , None , None , None)

def p_cond_clause(p):
    '''cond_clause : cond_part m  statement_s n 
    '''
    backpatch(p[1]["truelist"] , p[2]["quad"])
    p[0] = deepcopy(p[1])
    p[0]["nextlist"] =  merge(p[3]["nextlist"] , p[4]["nextlist"])


    if (Debug1) : print "Rule Declared: 115"

def p_cond_part(p):
    '''cond_part : condition THEN
    '''
    p[0] = deepcopy(p[1]) #Lists copied

    if (Debug1) : print "Rule Declared: 116"

def p_condition(p):
    '''condition : expression
    '''

    if (p[1]["type"] == "BOOL"):
        p[0] = p[1]
    else:
        print "[Condition Type] Error : Condition is not of Boolean type"
        p_error(p)
        p[0] = {'isarray': False, 'falselist': [], 'truelist': [], 'value': None, 'lexeme': None, 'type': None}



    if (Debug1) : print "Rule Declared: 117"

def p_else_opt(p):
    '''else_opt :
       | ELSE m statement_s
    '''
    p[0] = {"nextlist" : [] }

    if(len(p) == 1):
        p[0]["quad"]  = three_addr_code.get_next_instr_no()
    else:
        p[0] = deepcopy(p[3])
        p[0]["quad"] = p[2]["quad"]

    if (Debug1) : print "Rule Declared: 118"


#============ SWITCH CASE ============ , SAME AS iF-ELSEIF-IF
def p_case_stmt(p):
    '''case_stmt : case_hdr pragma_s alternative_s END CASE ';'
    '''
    if (Debug1) : print "Rule Declared: 119"


def p_case_hdr(p):
    '''case_hdr : CASE expression IS
    '''
    if (Debug1) : print "Rule Declared: 120"


def p_alternative_s(p):
    '''alternative_s :
       | alternative_s alternative
    '''
    if (Debug1) : print "Rule Declared: 121"


def p_alternative(p):
    '''alternative : WHEN choice_s ARROW statement_s
    '''
    if (Debug1) : print "Rule Declared: 122"


#===========================ALL DONE AFTER THIS=====================================
def p_loop_stmt(p):
    '''loop_stmt : label_opt iteration m basic_loop id_opt ';'
    '''
    #Add constraint
    if(p[2] != None):
        if (p[1] != None and p[5] != None ):
            if (p[1]["lexeme"] != p[5]["lexeme"]):
                if (debug2) : print "label matched"
                print "[Loop Structure] Error : the loop label and end statement label do not match"
                p_error(p)


        p[0] = deepcopy(p[4])
        backpatch(p[4]["nextlist"] , p[2]["quad"])
        three_addr_code.emit("goto" , p[2]["quad"] , None , None)

        if not p[2]["isinfinite"] :
            backpatch(p[2]["truelist"] , p[3]["quad"])
            p[0]["nextlist"] = p[2]["falselist"]

        if (Debug1) : print "Rule Declared: 123"

def p_label_opt(p):
    '''label_opt :
       | IDENTIFIER ':'
    '''
    if(len(p) == 3):
        if (p[1] in reserved):
            print "[Loop Labelling] Error : " + p[1] + " is a reserved keyword in Ada"
            p_error(p)

        elif (symbol_table.locate_Symbol_in_this(p[1])):
            print "[Loop Labelling] Error : " + p[1] + " is declared before. Can not be used again"
            p_error(p)

        else:
            p[0] = {"lexeme" : p[1]}
            symbol_table.createSym(p[1] , {"isloop" : True , "lexeme" : p[1]})

    else:
        p[0] = None

    if (Debug1) : print "Rule Declared: 124"

def p_iteration1(p):
    '''iteration :
       | WHILE m condition
    '''
    if (len(p) == 1) : #For Loop
        if (Debug2) : print "In Infinite loop"
        p[0] = {"quad" : three_addr_code.get_next_instr_no() , "isinfinite" : True}

    else : #While Loop 
        p[0] = deepcopy(p[3]) #backpactching lists are copied here
        p[0]["quad"] = p[2]["quad"] #Saving the address of this while loop 
        p[0]["isinfinite"] = False
    
    if (Debug1) : print "Rule Declared: 125"

def p_iteration2(p):
    '''iteration :  iter_part reverse_opt discrete_range
    '''
    #p[2] may be None or not
    if(Debug2) : print "In for loop"

    if (p[3] == None):
        print "[Range Format] Error : Range not defined properly for loop"
        p_error(p)

    else : 
        p[0] = {"isinfinite" : False}
        if(p[1] != None):
            if(p[2] == None): #reverse not used

                three_addr_code.emit(p[1]["lexeme"] , p[3]["lower_limit"] , ":=" , None)
                three_addr_code.emit("goto" , three_addr_code.get_next_instr_no() + 2, None , None )
                p[0]["quad"] = three_addr_code.get_next_instr_no()
                three_addr_code.emit(p[1]["lexeme"] , p[1]["lexeme"] , "+" , 1)
                p[0]["truelist"] = makeList(three_addr_code.get_next_instr_no())
                p[0]["falselist"] = makeList(three_addr_code.get_next_instr_no() + 1)
                three_addr_code.emit("blteq" , p[1]["lexeme"] , p[3]["upper_limit"] , None)
                three_addr_code.emit("goto" , None , None , None) 

            else:
                three_addr_code.emit(p[1]["lexeme"] , p[3]["lower_limit"] , ":=" , None)
                three_addr_code.emit("goto" , three_addr_code.get_next_instr_no() + 2, None , None )
                p[0]["quad"] = three_addr_code.get_next_instr_no()
                three_addr_code.emit(p[1]["lexeme"] , p[1]["lexeme"] , "-" , 1)
                p[0]["truelist"] = makeList(three_addr_code.get_next_instr_no())
                p[0]["falselist"] = makeList(three_addr_code.get_next_instr_no() + 1)
                three_addr_code.emit("bgteq" , p[1]["lexeme"] , p[3]["upper_limit"] , None)
                three_addr_code.emit("goto" , None , None , None) 

        else:
            p[0] = {"quad" : three_addr_code.get_next_instr_no() , "truelist" : [] , "falselist" : []  , "type" : None , "isinfinite" : False}
            if (Debug2) : print "Reverse Loop"

    if (Debug1) : print "Rule Declared: 125"

def p_iter_part(p):
    '''iter_part : FOR IDENTIFIER IN
    '''
    if (Debug1) : print "Rule Declared: 126"
    if (symbol_table.locate_Symbol(p[2])):
        print "[Loop Variable] Error : " + p[2] + " has already been declared"
        p_error(p)
    else:
        p[0]  = {"lexeme" : p[2] , "value" : None}
        symbol_table.createSym(p[2] , {"value" : None})

def p_reverse_opt(p):
    '''reverse_opt :
       | REVERSE
    '''
    if(len(p) == 1):
        p[0] = None
    else:
        p[0] = p[1]
    if (Debug1) : print "Rule Declared: 127"

def p_basic_loop(p):
    '''basic_loop : LOOP statement_s END LOOP
    '''
    p[0] = deepcopy(p[2])
    if (Debug1) : print "Rule Declared: 128"

def p_id_opt(p):
    '''id_opt :
       | designator
    '''
    if(len(p) == 1):
        p[0] = None
    else:
        p[0] = p[1]
    if (Debug1) : print "Rule Declared: 129"

#===============================================================================================

def p_block(p):
    '''block : label_opt block_decl block_body END id_opt ';'
    '''
    if (p[1] != None and p[5] != None ):
        if (p[1]["lexeme"] != p[5]["lexeme"]):
            if (debug2) : print "label matched"
            print "[Loop Structure] Error : the loop label and end statement label do not match"
            p_error(p)
    else:
        p[0] = p[3]

    if (Debug1) : print "Rule Declared: 130"

##***************** ADD DECLARATION CAPABILITIES HERE *********************************************
def p_block_decl(p):
    '''block_decl :
       | DECLARE decl_part
    '''
    if(len(p) == 1):
        p[0] = None
    else:
        if(Debug2) : print "TO BE DONE"

    if (Debug2) : print "Block Created"
    if (Debug1) : print "Rule Declared: 131"


def p_block_body(p):
    '''block_body : BEGIN handled_stmt_s
    '''
    p[0] = deepcopy(p[2])
    if (Debug1) : print "Rule Declared: 132"


def p_handled_stmt_s(p):
    '''handled_stmt_s : statement_s except_handler_part_opt 
    '''
    if(p[2] == None):
        p[0] = deepcopy(p[1])

    else:
        print "[Exception Block] Error : Exceptions are not handled"
        p_error(p)

    if (Debug1) : print "Rule Declared: 133"


def p_except_handler_part_opt(p):
    '''except_handler_part_opt :
       | except_handler_part
    '''
    if(len(p) == 1):
        p[0] = None 
    else :
        print "[Exception Block] Error : Exceptions are not handled"
        p_error(p)

    if (Debug1) : print "Rule Declared: 134"


def p_exit_stmt(p):
    '''exit_stmt : EXIT name_opt when_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 135"


def p_name_opt(p):
    '''name_opt :
       | name
    '''
    if (len(p) == 1):
        p[0] = None
    else:
        p[0] = p[1]
    if (Debug1) : print "Rule Declared: 136"


def p_when_opt(p):
    '''when_opt :
       | WHEN condition
    '''
    if (Debug1) : print "Rule Declared: 137"


def p_return_stmt(p):
    '''return_stmt : RETURN ';'
       | RETURN expression ';'
    '''
    if (Debug1) : print "Rule Declared: 138"


def p_goto_stmt(p):
    '''goto_stmt : GOTO name ';'
    '''
    if (Debug1) : print "Rule Declared: 139"


def p_subprog_decl(p):
    '''subprog_decl : subprog_spec ';'
       | generic_subp_inst ';'
       | subprog_spec_is_push ABSTRACT ';'
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 140"


def p_subprog_spec(p):
    '''subprog_spec : PROCEDURE compound_name formal_part_opt
       | FUNCTION designator formal_part_opt RETURN name
       | FUNCTION designator
    '''
    if(len(p) == 4):
        if (Debug2) : print "procedure defined " + str(p[2])

        if (p[2]["lexeme"] in reserved):
            print "[Procedure Declaration] Error : " + p[2]["lexeme"] + " is a reserved keyword in Ada"
            p_error(p)

        elif (symbol_table.locate_Symbol_in_this(p[2]["lexeme"])):
            print "[Procedure Declaration] Error : " + p[2]["lexeme"] + " is declared before. Can not be used again"
            p_error(p)

        p[0] = deepcopy(p[2])
        p[0]["var_List"] = []
        if (p[3] != None):
            p[0]["var_List"] = p[3]["var_List"]


    if (Debug1) : print "Rule Declared: 141"


def p_designator(p):
    '''designator : compound_name
       | STRING
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 142"


def p_formal_part_opt(p):
    '''formal_part_opt : 
       | formal_part
    '''
    if (len(p) == 1):
        p[0] = None 
    else:
        p[0] = deepcopy(p[1])

    if (Debug1) : print "Rule Declared: 143"


def p_formal_part(p):
    '''formal_part : '(' param_s ')'
    '''
    var_List = deepcopy(p[2])
    p[0] = {"var_List" : var_List}
    if (Debug1) : print "Rule Declared: 144"


#Only dictionaries flow here
def p_param_s(p):
    '''param_s : param
       | param_s ';' param
    '''
    if(len(p) == 2):
        p[0] = deepcopy(p[1])
    else:
        p[0] = p[1] + p[3]

    if (Debug1) : print "Rule Declared: 145"


def p_param(p):
    '''param : def_id_s ':' mode mark init_opt
       | error
    '''
    p[0] = []

    if(len(p) == 6):
        #def_id_s is a list of variables/ lexemes 
        if(p[4] != None ):
            if p[4]["istype"]:

                for item in p[1]:
                    dictionary = {"paramtype" : p[3] , "lexeme":item , "isarray":False, "type":symbol_table.get_Attribute_Value(p[4]["lexeme"] , "type")}
                    if (p[5] != None):
                        dictionary["value"] = p[5]["value"]  #Initial value
                    p[0].append({"name" : item , "dictionary" : dictionary})

            else:
                print "[Procedure Declaration] Error : " + p[4]["lexeme"] +" is not a valid type "
        else:
            print "[Procedure Declaration] Error : Parameter Types not given"
            p_error(p)

    else: 
        print "not handled yet"
    if (Debug1) : print "Rule Declared: 146"


def p_mode(p):
    '''mode :
       | IN
       | OUT
       | IN OUT
       | ACCESS
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif (len(p) == 1) : p[0] = None
    else:
        p[0] = p[1] + p[2]

    if (Debug1) : print "Rule Declared: 147"


def p_subprog_spec_is_push(p):
    '''subprog_spec_is_push : subprog_spec IS
    '''
    p[0] = deepcopy(p[1])

    p[0]["nextlist"] = []

    if(symbol_table.get_current_table().prev_table != None):  #going out/back/ used while calling
        p[0]["nextlist"] = [three_addr_code.get_next_instr_no()]
        #three_addr_code.emit("goto" , None , None , None )

    symbol_table.begin_scope()
    symbol_table.declare_Procedure(p[1]["lexeme"] , p[1]["var_List"])
    three_addr_code.emit("proc_label" , p[1]["lexeme"] ,None , None )

    if (Debug1) : print "Rule Declared: 148"


def p_subprog_body(p):
    '''subprog_body : subprog_spec_is_push decl_part block_body END id_opt ';'
    '''
    if(p[5] != None):
        if(p[1]["lexeme"] != p[5]["lexeme"]):
            print "[Procedure Declaration] Error : labels at the end of procedure block do not match"
            p_error(p)

    p[0] = deepcopy(p[3])

    outvars = ""
    for item in symbol_table.get_Hash_Table():
        if(symbol_table.get_Attribute_Value(item , "paramtype") == "out"):
            outvars += " " + symbol_table.get_Attribute_Value(item ,"lexeme")
    #In the symbol table of the procedure

    if (outvars != ""):
        three_addr_code.emit("return" , outvars , None , None )
    else:
        three_addr_code.emit("return" , None , None , None)

    symbol_table.end_scope()

    if(p[0] != None):
        backpatch(p[0]["nextlist"] , three_addr_code.get_next_instr_no() - 1)
    else:
        print "None statement propagating"
    if (Debug1) : print "Rule Declared: 149"


def p_procedure_call(p):
    '''procedure_call : name ';'
    '''
    p[0] = deepcopy(p[1])
    p[0]["nextlist"] = []

    if (Debug1) : print "Rule Declared: 150"

def p_pkg_decl(p):
    '''pkg_decl : pkg_spec ';'
       | generic_pkg_inst ';'
    '''
    if (Debug1) : print "Rule Declared: 151"


def p_pkg_spec(p):
    '''pkg_spec : PACKAGE compound_name IS decl_item_s private_part END c_id_opt
    '''
    if (Debug1) : print "Rule Declared: 152"


def p_private_part(p):
    '''private_part :
       | PRIVATE decl_item_s
    '''
    if (Debug1) : print "Rule Declared: 153"


def p_c_id_opt(p):
    '''c_id_opt : 
       | compound_name
    '''
    if (Debug1) : print "Rule Declared: 154"


def p_pkg_body(p):
    '''pkg_body : PACKAGE BODY compound_name IS decl_part body_opt END c_id_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 155"


def p_body_opt(p):
    '''body_opt :
       | block_body
    '''
    if (Debug1) : print "Rule Declared: 156"


def p_private_type(p):
    '''private_type : tagged_opt limited_opt PRIVATE
    '''
    if (Debug1) : print "Rule Declared: 157"


def p_limited_opt(p):
    '''limited_opt :
       | LIMITED
    '''
    if (Debug1) : print "Rule Declared: 158"


def p_use_clause(p):
    '''use_clause : USE name_s ';'
       | USE TYPE name_s ';'
    '''
    if (Debug1) : print "Rule Declared: 159"


def p_name_s(p):
    '''name_s : name
       | name_s ',' name
    '''
    if(len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
    if (Debug1) : print "Rule Declared: 160"


def p_rename_decl(p):
    '''rename_decl : def_id_s ':' object_qualifier_opt subtype_ind renames ';'
       | def_id_s ':' EXCEPTION renames ';'
       | rename_unit
    '''
    if (Debug1) : print "Rule Declared: 161"


def p_rename_unit(p):
    '''rename_unit : PACKAGE compound_name renames ';'
       | subprog_spec renames ';'
       | generic_formal_part PACKAGE compound_name renames ';'
       | generic_formal_part subprog_spec renames ';'
    '''
    if (Debug1) : print "Rule Declared: 162"


def p_renames(p):
    '''renames : RENAMES name
    '''
    if (Debug1) : print "Rule Declared: 163"


def p_task_decl(p):
    '''task_decl : task_spec ';'
    '''
    if (Debug1) : print "Rule Declared: 164"


def p_task_spec(p):
    '''task_spec : TASK simple_name task_def
       | TASK TYPE simple_name discrim_part_opt task_def
    '''
    if (Debug1) : print "Rule Declared: 165"


def p_task_def(p):
    '''task_def :
       | IS entry_decl_s rep_spec_s task_private_opt END id_opt
    '''
    if (Debug1) : print "Rule Declared: 166"


def p_task_private_opt(p):
    '''task_private_opt :
       | PRIVATE entry_decl_s rep_spec_s
    '''
    if (Debug1) : print "Rule Declared: 167"


def p_task_body(p):
    '''task_body : TASK BODY simple_name IS decl_part block_body END id_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 168"


def p_prot_decl(p):
    '''prot_decl : prot_spec ';'
    '''
    if (Debug1) : print "Rule Declared: 169"


def p_prot_spec(p):
    '''prot_spec : PROTECTED IDENTIFIER prot_def
       | PROTECTED TYPE simple_name discrim_part_opt prot_def
    '''
    if (Debug1) : print "Rule Declared: 170"


def p_prot_def(p):
    '''prot_def : IS prot_op_decl_s prot_private_opt END id_opt
    '''
    if (Debug1) : print "Rule Declared: 171"


def p_prot_private_opt(p):
    '''prot_private_opt :
       | PRIVATE prot_elem_decl_s 
    '''
    if (Debug1) : print "Rule Declared: 172"


def p_prot_op_decl_s(p):
    '''prot_op_decl_s : 
       | prot_op_decl_s prot_op_decl
    '''
    if (Debug1) : print "Rule Declared: 173"


def p_prot_op_decl(p):
    '''prot_op_decl : entry_decl
       | subprog_spec ';'
       | rep_spec
       | pragma
    '''
    if (Debug1) : print "Rule Declared: 174"


def p_prot_elem_decl_s(p):
    '''prot_elem_decl_s : 
       | prot_elem_decl_s prot_elem_decl
    '''
    if (Debug1) : print "Rule Declared: 175"


def p_prot_elem_decl(p):
    '''prot_elem_decl : prot_op_decl 
    | comp_decl
    '''
    if (Debug1) : print "Rule Declared: 176"


def p_prot_body(p):
    '''prot_body : PROTECTED BODY simple_name IS prot_op_body_s END id_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 177"


def p_prot_op_body_s(p):
    '''prot_op_body_s : pragma_s
       | prot_op_body_s prot_op_body pragma_s
    '''
    if (Debug1) : print "Rule Declared: 178"


def p_prot_op_body(p):
    '''prot_op_body : entry_body
       | subprog_body
       | subprog_spec ';'
    '''
    if (Debug1) : print "Rule Declared: 179"


def p_entry_decl_s(p):
    '''entry_decl_s : pragma_s
       | entry_decl_s entry_decl pragma_s
    '''
    if (Debug1) : print "Rule Declared: 180"


def p_entry_decl(p):
    '''entry_decl : ENTRY IDENTIFIER formal_part_opt ';'
       | ENTRY IDENTIFIER '(' discrete_range ')' formal_part_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 181"


def p_entry_body(p):
    '''entry_body : ENTRY IDENTIFIER formal_part_opt WHEN condition entry_body_part
       | ENTRY IDENTIFIER '(' iter_part discrete_range ')' formal_part_opt WHEN condition entry_body_part
    '''
    if (Debug1) : print "Rule Declared: 182"


def p_entry_body_part(p):
    '''entry_body_part : ';'
       | IS decl_part block_body END id_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 183"


def p_rep_spec_s(p):
    '''rep_spec_s :
       | rep_spec_s rep_spec pragma_s
    '''
    if (Debug1) : print "Rule Declared: 184"


def p_entry_call(p):
    '''entry_call : procedure_call
    '''
    if (Debug1) : print "Rule Declared: 185"


def p_accept_stmt(p):
    '''accept_stmt : accept_hdr ';'
       | accept_hdr DO handled_stmt_s END id_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 186"


def p_accept_hdr(p):
    '''accept_hdr : ACCEPT entry_name formal_part_opt
    '''
    if (Debug1) : print "Rule Declared: 187"


def p_entry_name(p):
    '''entry_name : simple_name
       | entry_name '(' expression ')'
    '''
    if (Debug1) : print "Rule Declared: 188"


def p_delay_stmt(p):
    '''delay_stmt : DELAY expression ';'
       | DELAY UNTIL expression ';'
    '''
    if (Debug1) : print "Rule Declared: 189"


def p_select_stmt(p):
    '''select_stmt : select_wait
       | async_select
       | timed_entry_call
       | cond_entry_call
    '''
    if (Debug1) : print "Rule Declared: 190"


def p_select_wait(p):
    '''select_wait : SELECT guarded_select_alt or_select else_opt  END SELECT ';'
    '''
    if (Debug1) : print "Rule Declared: 191"


def p_guarded_select_alt(p):
    '''guarded_select_alt : select_alt
       | WHEN condition ARROW select_alt
    '''
    if (Debug1) : print "Rule Declared: 192"


def p_or_select(p):
    '''or_select :
       | or_select OR guarded_select_alt
    '''
    if (Debug1) : print "Rule Declared: 193"


def p_select_alt(p):
    '''select_alt : accept_stmt stmts_opt
       | delay_stmt stmts_opt
       | TERMINATE ';'
    '''
    if (Debug1) : print "Rule Declared: 194"


def p_delay_or_entry_alt(p):
    '''delay_or_entry_alt : delay_stmt stmts_opt
       | entry_call stmts_opt
    '''
    if (Debug1) : print "Rule Declared: 195"


def p_async_select(p):
    '''async_select : SELECT delay_or_entry_alt THEN ABORT statement_s END SELECT ';'
    '''
    if (Debug1) : print "Rule Declared: 196"


def p_timed_entry_call(p):
    '''timed_entry_call : SELECT entry_call stmts_opt OR delay_stmt stmts_opt END SELECT ';'
    '''
    if (Debug1) : print "Rule Declared: 197"


def p_cond_entry_call(p):
    '''cond_entry_call : SELECT entry_call stmts_opt ELSE statement_s END SELECT ';'
    '''
    if (Debug1) : print "Rule Declared: 198"


def p_stmts_opt(p):
    '''stmts_opt :
       | statement_s
    '''
    if (Debug1) : print "Rule Declared: 199"


def p_abort_stmt(p):
    '''abort_stmt : ABORT name_s ';'
    '''
    if (Debug1) : print "Rule Declared: 200"


def p_compilation(p):
    '''compilation :
       | compilation comp_unit
       | pragma pragma_s
    '''
    if(len(p) == 1):
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]
    if (Debug1) : print "Rule Declared: 201"


def p_comp_unit(p):
    '''comp_unit : context_spec private_opt unit pragma_s
       | private_opt unit pragma_s
    '''
    if(len(p) == 4):
        p[0] = p[2]
    else:
        p[0] = p[3]
    if (Debug1) : print "Rule Declared: 202"


def p_private_opt(p):
    '''private_opt :
       | PRIVATE
    '''
    if (Debug1) : print "Rule Declared: 203"


def p_context_spec(p):
    '''context_spec : with_clause use_clause_opt
       | context_spec with_clause use_clause_opt
       | context_spec pragma
    '''
    if (Debug1) : print "Rule Declared: 204"


def p_with_clause(p):
    '''with_clause : WITH c_name_list ';'
    '''
    if (Debug1) : print "Rule Declared: 205"


def p_use_clause_opt(p):
    '''use_clause_opt :
       | use_clause_opt use_clause
    '''
    if (Debug1) : print "Rule Declared: 206"


def p_unit(p):
    '''unit : pkg_decl
       | pkg_body
       | subprog_decl
       | subprog_body
       | subunit
       | generic_decl
       | rename_unit
    '''
    p[0] = deepcopy(p[1])
    if (Debug1) : print "Rule Declared: 207"


def p_subunit(p):
    '''subunit : SEPARATE '(' compound_name ')' subunit_body
    '''
    if (Debug1) : print "Rule Declared: 208"


def p_subunit_body(p):
    '''subunit_body : subprog_body
       | pkg_body
       | task_body
       | prot_body
    '''
    p[0] = deepcopys(p[1])
    if (Debug1) : print "Rule Declared: 209"


def p_body_stub(p):
    '''body_stub : TASK BODY simple_name IS SEPARATE ';'
       | PACKAGE BODY compound_name IS SEPARATE ';'
       | subprog_spec IS SEPARATE ';'
       | PROTECTED BODY simple_name IS SEPARATE ';'
    '''
    if (Debug1) : print "Rule Declared: 210"


def p_exception_decl(p):
    '''exception_decl : def_id_s ':' EXCEPTION ';'
    '''
    if (Debug1) : print "Rule Declared: 211"


def p_except_handler_part(p):
    '''except_handler_part : EXCEPTION exception_handler
       | except_handler_part exception_handler
    '''
    if (Debug1) : print "Rule Declared: 212"


def p_exception_handler(p):
    '''exception_handler : WHEN except_choice_s ARROW statement_s
       | WHEN IDENTIFIER ':' except_choice_s ARROW statement_s
    '''
    if (Debug1) : print "Rule Declared: 213"


def p_except_choice_s(p):
    '''except_choice_s : except_choice
       | except_choice_s '|' except_choice
    '''
    if (Debug1) : print "Rule Declared: 214"


def p_except_choice(p):
    '''except_choice : name
       | OTHERS
    '''
    if (Debug1) : print "Rule Declared: 215"


def p_raise_stmt(p):
    '''raise_stmt : RAISE name_opt ';'
    '''
    if (Debug1) : print "Rule Declared: 216"


def p_requeue_stmt(p):
    '''requeue_stmt : REQUEUE name ';'
       | REQUEUE name WITH ABORT ';'
    '''
    if (Debug1) : print "Rule Declared: 217"


def p_generic_decl(p):
    '''generic_decl : generic_formal_part subprog_spec ';'
       | generic_formal_part pkg_spec ';'
    '''
    if (Debug1) : print "Rule Declared: 218"


def p_generic_formal_part(p):
    '''generic_formal_part : GENERIC
       | generic_formal_part generic_formal
    '''
    if (Debug1) : print "Rule Declared: 219"


def p_generic_formal(p):
    '''generic_formal : param ';'
       | TYPE simple_name generic_discrim_part_opt IS generic_type_def ';'
       | WITH PROCEDURE simple_name formal_part_opt subp_default ';'
       | WITH FUNCTION designator formal_part_opt RETURN name subp_default ';'
       | WITH PACKAGE simple_name IS NEW name '(' LESSMORE ')' ';'
       | WITH PACKAGE simple_name IS NEW name ';'
       | use_clause
    '''
    if (Debug1) : print "Rule Declared: 220"


def p_generic_discrim_part_opt(p):
    '''generic_discrim_part_opt :
       | discrim_part
       | '(' LESSMORE ')'
    '''
    if (Debug1) : print "Rule Declared: 221"


def p_subp_default(p):
    '''subp_default :
       | IS name
       | IS LESSMORE
    '''
    if (Debug1) : print "Rule Declared: 222"


def p_generic_type_def(p):
    '''generic_type_def : '(' LESSMORE ')'
       | RANGE LESSMORE
       | MOD LESSMORE
       | DELTA LESSMORE
       | DELTA LESSMORE DIGITS LESSMORE
       | DIGITS LESSMORE
       | array_type
       | access_type
       | private_type
       | generic_derived_type
    '''
    if (Debug1) : print "Rule Declared: 223"


def p_generic_derived_type(p):
    '''generic_derived_type : NEW subtype_ind
       | NEW subtype_ind WITH PRIVATE
       | ABSTRACT NEW subtype_ind WITH PRIVATE
    '''
    if (Debug1) : print "Rule Declared: 224"


def p_generic_subp_inst(p):
    '''generic_subp_inst : subprog_spec IS generic_inst
    '''
    if (Debug1) : print "Rule Declared: 225"


def p_generic_pkg_inst(p):
    '''generic_pkg_inst : PACKAGE compound_name IS generic_inst
    '''
    if (Debug1) : print "Rule Declared: 226"


def p_generic_inst(p):
    '''generic_inst : NEW name
    '''
    if (Debug1) : print "Rule Declared: 227"


def p_rep_spec(p):
    '''rep_spec : attrib_def
       | record_type_spec
       | address_spec
    '''
    if (Debug1) : print "Rule Declared: 228"


def p_attrib_def(p):
    '''attrib_def : FOR mark USE expression ';'
    '''
    if (Debug1) : print "Rule Declared: 229"


def p_record_type_spec(p):
    '''record_type_spec : FOR mark USE RECORD align_opt comp_loc_s END RECORD ';'
    '''
    if (Debug1) : print "Rule Declared: 230"


def p_align_opt(p):
    '''align_opt :
       | AT MOD expression ';'
    '''
    if (Debug1) : print "Rule Declared: 231"


def p_comp_loc_s(p):
    '''comp_loc_s :
       | comp_loc_s mark AT expression RANGE range ';'
    '''
    if (Debug1) : print "Rule Declared: 232"


def p_address_spec(p):
    '''address_spec : FOR mark USE AT expression ';'
    '''
    if (Debug1) : print "Rule Declared: 233"

##TO BE CHANGED
def p_code_stmt(p):
    '''code_stmt : qualified ';'
    '''
    if (Debug1) : print "Rule Declared: 234"
    
def p_error(p):
    if (hasattr(p,'type')):
        print "[Parsing] Error at line ",p.lineno,": Token:",p.type,"incorrectly parsed" 
    global success
    success = False
    parser.errok()


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
        if (Debug3) : result = parser.parse(data , debug = 1)
        else : result = parser.parse(data)

    global success
    print success
    if (success) : three_addr_code.print_structures()

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissions!"
