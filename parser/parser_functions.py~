#This has been automatically generted using http://www.adaic.org/resources/add_content/standards/95lrm/grammar9x.y
#Semantics have been added manually

Debug1 = False

def p_start_symbol(p):
	'''start_symbol : compilation
    	'''
	p[0]=p[1]
	if (Debug1) : print "Rule Used:1"

def p_pragma(p):
	'''pragma  : PRAGMA IDENTIFIER ';'
	   | PRAGMA simple_name '(' pragma_arg_s ')' ';'
	'''
	if (Debug1) : print "Rule Used:2"


def p_pragma_arg_s(p):
	'''pragma_arg_s : pragma_arg
	   | pragma_arg_s ',' pragma_arg
	'''
	if (Debug1) : print "Rule Used:3"


def p_pragma_arg(p):
	'''pragma_arg : expression
	   | simple_name ARROW expression
	'''
	if (Debug1) : print "Rule Used:4"


def p_pragma_s(p):
	'''pragma_s :
	   | pragma_s pragma
	'''
	if (Debug1) : print "Rule Used:5"


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
	if (Debug1) : print "Rule Used:6"


def p_object_decl(p):
	'''object_decl : def_id_s ':' object_qualifier_opt object_subtype_def init_opt ';'
	'''
	if (Debug1) : print "Rule Used:7"


def p_def_id_s(p):
	'''def_id_s : def_id
	   | def_id_s ',' def_id
	'''
	if (Debug1) : print "Rule Used:8"


def p_def_id(p):
	'''def_id  : IDENTIFIER
	'''
	if (Debug1) : print "Rule Used:9"


def p_object_qualifier_opt(p):
	'''object_qualifier_opt :
	   | ALIASED
	   | CONSTANT
	   | ALIASED CONSTANT
	'''
	if (Debug1) : print "Rule Used:10"


def p_object_subtype_def(p):
	'''object_subtype_def : subtype_ind
	   | array_type
	'''
	if (Debug1) : print "Rule Used:11"


def p_init_opt(p):
	'''init_opt :
	   | ASSIGNMENT expression
	'''
	if (Debug1) : print "Rule Used:12"


def p_number_decl(p):
	'''number_decl : def_id_s ':' CONSTANT ASSIGNMENT expression ';'
	'''
	if (Debug1) : print "Rule Used:13"


def p_type_decl(p):
	'''type_decl : TYPE IDENTIFIER discrim_part_opt type_completion ';'
	'''
	if (Debug1) : print "Rule Used:14"


def p_discrim_part_opt(p):
	'''discrim_part_opt :
	   | discrim_part
	   | '(' LESSMORE ')'
	'''
	if (Debug1) : print "Rule Used:15"


def p_type_completion(p):
	'''type_completion :
	   | IS type_def
	'''
	if (Debug1) : print "Rule Used:16"


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
	if (Debug1) : print "Rule Used:17"


def p_subtype_decl(p):
	'''subtype_decl : SUBTYPE IDENTIFIER IS subtype_ind ';'
	'''
	if (Debug1) : print "Rule Used:18"


def p_subtype_ind(p):
	'''subtype_ind : name constraint
	   | name
	'''
	if (Debug1) : print "Rule Used:19"


def p_constraint(p):
	'''constraint : range_constraint
	   | decimal_digits_constraint
	'''
	if (Debug1) : print "Rule Used:20"


def p_decimal_digits_constraint(p):
	'''decimal_digits_constraint : DIGITS expression range_constr_opt
	'''
	if (Debug1) : print "Rule Used:21"


def p_derived_type(p):
	'''derived_type : NEW subtype_ind
	   | NEW subtype_ind WITH PRIVATE
	   | NEW subtype_ind WITH record_def
	   | ABSTRACT NEW subtype_ind WITH PRIVATE
	   | ABSTRACT NEW subtype_ind WITH record_def
	'''
	if (Debug1) : print "Rule Used:22"


def p_range_constraint(p):
	'''range_constraint : RANGE range
	'''
	if (Debug1) : print "Rule Used:23"


def p_range(p):
	'''range : simple_expression DOTDOT simple_expression
	   | name TICK RANGE
	   | name TICK RANGE '(' expression ')'
	'''
	if (Debug1) : print "Rule Used:24"


def p_enumeration_type(p):
	'''enumeration_type : '(' enum_id_s ')'
	'''
	if (Debug1) : print "Rule Used:25"


def p_enum_id_s(p):
	'''enum_id_s : enum_id
	   | enum_id_s ',' enum_id
	'''
	if (Debug1) : print "Rule Used:26"


def p_enum_id(p):
	'''enum_id : IDENTIFIER
	   | CHAR
	'''
	if (Debug1) : print "Rule Used:27"


def p_integer_type(p):
	'''integer_type : range_spec
	   | MOD expression
	'''
	if (Debug1) : print "Rule Used:28"


def p_(p):
	'''    
	'''
	if (Debug1) : print "Rule Used:29"


def p_range_spec(p):
	'''range_spec : range_constraint
	'''
	if (Debug1) : print "Rule Used:30"


def p_range_spec_opt(p):
	'''range_spec_opt :
	   | range_spec
	'''
	if (Debug1) : print "Rule Used:31"


def p_real_type(p):
	'''real_type : float_type
	   | fixed_type
	'''
	if (Debug1) : print "Rule Used:32"


def p_float_type(p):
	'''float_type : DIGITS expression range_spec_opt
	'''
	if (Debug1) : print "Rule Used:33"


def p_fixed_type(p):
	'''fixed_type : DELTA expression range_spec
	   | DELTA expression DIGITS expression range_spec_opt
	'''
	if (Debug1) : print "Rule Used:34"


def p_array_type(p):
	'''array_type : unconstr_array_type
	   | constr_array_type
	'''
	if (Debug1) : print "Rule Used:35"


def p_unconstr_array_type(p):
	'''unconstr_array_type : ARRAY '(' index_s ')' OF component_subtype_def
	'''
	if (Debug1) : print "Rule Used:36"


def p_constr_array_type(p):
	'''constr_array_type : ARRAY iter_index_constraint OF component_subtype_def
	'''
	if (Debug1) : print "Rule Used:37"


def p_component_subtype_def(p):
	'''component_subtype_def : aliased_opt subtype_ind
	'''
	if (Debug1) : print "Rule Used:38"


def p_aliased_opt(p):
	'''aliased_opt : 
	   | ALIASED
	'''
	if (Debug1) : print "Rule Used:39"


def p_index_s(p):
	'''index_s : index
	   | index_s ',' index
	'''
	if (Debug1) : print "Rule Used:40"


def p_index(p):
	'''index : name RANGE LESSMORE
	'''
	if (Debug1) : print "Rule Used:41"


def p_iter_index_constraint(p):
	'''iter_index_constraint : '(' iter_discrete_range_s ')'
	'''
	if (Debug1) : print "Rule Used:42"


def p_iter_discrete_range_s(p):
	'''iter_discrete_range_s : discrete_range
	   | iter_discrete_range_s ',' discrete_range
	'''
	if (Debug1) : print "Rule Used:43"


def p_discrete_range(p):
	'''discrete_range : name range_constr_opt
	   | range
	'''
	if (Debug1) : print "Rule Used:44"


def p_range_constr_opt(p):
	'''range_constr_opt :
	   | range_constraint
	'''
	if (Debug1) : print "Rule Used:45"


def p_record_type(p):
	'''record_type : tagged_opt limited_opt record_def
	'''
	if (Debug1) : print "Rule Used:46"


def p_record_def(p):
	'''record_def : RECORD pragma_s comp_list END RECORD
	   | NuLL RECORD
	'''
	if (Debug1) : print "Rule Used:47"


def p_tagged_opt(p):
	'''tagged_opt :
	   | TAGGED
	   | ABSTRACT TAGGED
	'''
	if (Debug1) : print "Rule Used:48"


def p_comp_list(p):
	'''comp_list : comp_decl_s variant_part_opt
	   | variant_part pragma_s
	   | NuLL ';' pragma_s
	'''
	if (Debug1) : print "Rule Used:49"


def p_comp_decl_s(p):
	'''comp_decl_s : comp_decl
	   | comp_decl_s pragma_s comp_decl
	'''
	if (Debug1) : print "Rule Used:50"


def p_variant_part_opt(p):
	'''variant_part_opt : pragma_s
	   | pragma_s variant_part pragma_s
	'''
	if (Debug1) : print "Rule Used:51"


def p_comp_decl(p):
	'''comp_decl : def_id_s ':' component_subtype_def init_opt ';'
	   | error ';'
	'''
	if (Debug1) : print "Rule Used:52"


def p_discrim_part(p):
	'''discrim_part : '(' discrim_spec_s ')'
	'''
	if (Debug1) : print "Rule Used:53"


def p_discrim_spec_s(p):
	'''discrim_spec_s : discrim_spec
	   | discrim_spec_s ';' discrim_spec
	'''
	if (Debug1) : print "Rule Used:54"


def p_discrim_spec(p):
	'''discrim_spec : def_id_s ':' access_opt mark init_opt
	   | error
	'''
	if (Debug1) : print "Rule Used:55"


def p_access_opt(p):
	'''access_opt :
	   | ACCESS
	'''
	if (Debug1) : print "Rule Used:56"


def p_variant_part(p):
	'''variant_part : CASE simple_name IS pragma_s variant_s END CASE ';'
	'''
	if (Debug1) : print "Rule Used:57"


def p_variant_s(p):
	'''variant_s : variant
	   | variant_s variant
	'''
	if (Debug1) : print "Rule Used:58"


def p_variant(p):
	'''variant : WHEN choice_s ARROW pragma_s comp_list
	'''
	if (Debug1) : print "Rule Used:59"


def p_choice_s(p):
	'''choice_s : choice
	   | choice_s '|' choice
	'''
	if (Debug1) : print "Rule Used:60"


def p_choice(p):
	'''choice : expression
	   | discrete_with_range
	   | OTHERS
	'''
	if (Debug1) : print "Rule Used:61"


def p_discrete_with_range(p):
	'''discrete_with_range : name range_constraint
	   | range
	'''
	if (Debug1) : print "Rule Used:62"


def p_access_type(p):
	'''access_type : ACCESS subtype_ind
	   | ACCESS CONSTANT subtype_ind
	   | ACCESS ALL subtype_ind
	   | ACCESS prot_opt PROCEDURE formal_part_opt
	   | ACCESS prot_opt FUNCTION formal_part_opt RETURN mark
	'''
	if (Debug1) : print "Rule Used:63"


def p_prot_opt(p):
	'''prot_opt :
	   | PROTECTED
	'''
	if (Debug1) : print "Rule Used:64"


def p_decl_part(p):
	'''decl_part :
	   | decl_item_or_body_s1
	'''
	if (Debug1) : print "Rule Used:65"


def p_decl_item_s(p):
	'''decl_item_s : 
	   | decl_item_s1
	'''
	if (Debug1) : print "Rule Used:66"


def p_decl_item_s1(p):
	'''decl_item_s1 : decl_item
	   | decl_item_s1 decl_item
	'''
	if (Debug1) : print "Rule Used:67"


def p_decl_item(p):
	'''decl_item : decl
	   | use_clause
	   | rep_spec
	   | pragma
	'''
	if (Debug1) : print "Rule Used:68"


def p_decl_item_or_body_s(p):
	'''decl_item_or_body_s1 : decl_item_or_body
	   | decl_item_or_body_s1 decl_item_or_body
	'''
	if (Debug1) : print "Rule Used:69"


def p_decl_item_or_body(p):
	'''decl_item_or_body : body
	   | decl_item
	'''
	if (Debug1) : print "Rule Used:70"


def p_body(p):
	'''body : subprog_body
	   | pkg_body
	   | task_body
	   | prot_body
	'''
	if (Debug1) : print "Rule Used:71"


def p_name(p):
	'''name : simple_name
	   | indexed_comp
	   | selected_comp
	   | attribute
	   | operator_symbol
	'''
	if (Debug1) : print "Rule Used:72"


def p_mark(p):
	'''mark : simple_name
	   | mark TICK attribute_id
	   | mark '.' simple_name
	'''
	if (Debug1) : print "Rule Used:73"


def p_simple_name(p):
	'''simple_name : IDENTIFIER
	'''
	if (Debug1) : print "Rule Used:74"


def p_compound_name(p):
	'''compound_name : simple_name
	   | compound_name '.' simple_name
	'''
	if (Debug1) : print "Rule Used:75"


def p_c_name_list(p):
	'''c_name_list : compound_name
	    | c_name_list ',' compound_name
	'''
	if (Debug1) : print "Rule Used:76"


def p_used_char(p):
	'''used_char : CHAR
	'''
	if (Debug1) : print "Rule Used:77"


def p_operator_symbol(p):
	'''operator_symbol : STRING
	'''
	if (Debug1) : print "Rule Used:78"


def p_indexed_comp(p):
	'''indexed_comp : name '(' value_s ')'
	'''
	if (Debug1) : print "Rule Used:79"


def p_value_s(p):
	'''value_s : value
	   | value_s ',' value
	'''
	if (Debug1) : print "Rule Used:80"


def p_value(p):
	'''value : expression
	   | comp_assoc
	   | discrete_with_range
	   | error
	'''
	if (Debug1) : print "Rule Used:81"


def p_selected_comp(p):
	'''selected_comp : name '.' simple_name
	   | name '.' used_char
	   | name '.' operator_symbol
	   | name '.' ALL
	'''
	if (Debug1) : print "Rule Used:82"


def p_attribute(p):
	'''attribute : name TICK attribute_id
	'''
	if (Debug1) : print "Rule Used:83"


def p_attribute_id(p):
	'''attribute_id : IDENTIFIER
	   | DIGITS
	   | DELTA
	   | ACCESS
	'''
	if (Debug1) : print "Rule Used:84"


def p_literal(p):
	'''literal : INTEGER
       | BASE_INTEGER
       | FLOAT
       | BASE_FLOAT
	   | used_char
	   | NuLL
	'''
	if (Debug1) : print "Rule Used:85"


def p_aggregate(p):
	'''aggregate : '(' comp_assoc ')'
	   | '(' value_s_2 ')'
	   | '(' expression WITH value_s ')'
	   | '(' expression WITH NuLL RECORD ')'
	   | '(' NuLL RECORD ')'
	'''
	if (Debug1) : print "Rule Used:86"


def p_value_s_(p):
	'''value_s_2 : value ',' value
	   | value_s_2 ',' value
	'''
	if (Debug1) : print "Rule Used:87"


def p_comp_assoc(p):
	'''comp_assoc : choice_s ARROW expression
	'''
	if (Debug1) : print "Rule Used:88"


def p_expression(p):
	'''expression : relation
	   | expression logical relation
	   | expression short_circuit relation
	'''
	if (Debug1) : print "Rule Used:89"


def p_logical(p):
	'''logical : AND
	   | OR
	   | XOR
	'''
	if (Debug1) : print "Rule Used:90"


def p_short_circuit(p):
	'''short_circuit : AND THEN
	   | OR ELSE
	'''
	if (Debug1) : print "Rule Used:91"


def p_relation(p):
	'''relation : simple_expression
	   | simple_expression relational simple_expression
	   | simple_expression membership range
	   | simple_expression membership name
	'''
	if (Debug1) : print "Rule Used:92"


def p_relational(p):
	'''relational : '='
	   | NOTEQUAL
	   | '<'
	   | LESSEQ
	   | '>'
	   | GREATEREQ
	'''
	if (Debug1) : print "Rule Used:93"


def p_membership(p):
	'''membership : IN
	   | NOT IN
	'''
	if (Debug1) : print "Rule Used:94"


def p_simple_expression(p):
	'''simple_expression : unary term
	   | term
	   | simple_expression adding term
	'''
	if (Debug1) : print "Rule Used:95"


def p_unary(p):
	'''unary   : '+'
	   | '-'
	'''
	if (Debug1) : print "Rule Used:96"


def p_adding(p):
	'''adding  : '+'
	   | '-'
	   | '&'
	'''
	if (Debug1) : print "Rule Used:97"


def p_term(p):
	'''term    : factor
	   | term multiplying factor
	'''
	if (Debug1) : print "Rule Used:98"


def p_multiplying(p):
	'''multiplying : '*'
	   | '/'
	   | MOD
	   | REM
	'''
	if (Debug1) : print "Rule Used:99"


def p_factor(p):
	'''factor : primary
	   | NOT primary
	   | ABS primary
	   | primary STARSTAR primary
	'''
	if (Debug1) : print "Rule Used:100"


def p_primary(p):
	'''primary : literal
	   | name
	   | allocator
	   | qualified
	   | parenthesized_primary
	'''
	if (Debug1) : print "Rule Used:101"


def p_parenthesized_primary(p):
	'''parenthesized_primary : aggregate
	   | '(' expression ')'
	'''
	if (Debug1) : print "Rule Used:102"


def p_qualified(p):
	'''qualified : name TICK parenthesized_primary
	'''
	if (Debug1) : print "Rule Used:103"


def p_allocator(p):
	'''allocator : NEW name
	   | NEW qualified
	'''
	if (Debug1) : print "Rule Used:104"


def p_statement_s(p):
	'''statement_s : statement
	   | statement_s statement
	'''
	if (Debug1) : print "Rule Used:105"


def p_statement(p):
	'''statement : unlabeled
	   | label statement
	'''
	if (Debug1) : print "Rule Used:106"


def p_unlabeled(p):
	'''unlabeled : simple_stmt
	   | compound_stmt
	   | pragma
	'''
	if (Debug1) : print "Rule Used:107"


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
	if (Debug1) : print "Rule Used:108"


def p_compound_stmt(p):
	'''compound_stmt : if_stmt
	   | case_stmt
	   | loop_stmt
	   | block
	   | accept_stmt
	   | select_stmt
	'''
	if (Debug1) : print "Rule Used:109"


def p_label(p):
	'''label : LESSLESS IDENTIFIER MOREMORE
	'''
	if (Debug1) : print "Rule Used:110"


def p_null_stmt(p):
	'''null_stmt : NuLL ';'
	'''
	if (Debug1) : print "Rule Used:111"


def p_assign_stmt(p):
	'''assign_stmt : name ASSIGNMENT expression ';'
	'''
	if (Debug1) : print "Rule Used:112"


def p_if_stmt(p):
	'''if_stmt : IF cond_clause_s else_opt END IF ';'
	'''
	if (Debug1) : print "Rule Used:113"


def p_cond_clause_s(p):
	'''cond_clause_s : cond_clause
	   | cond_clause_s ELSIF cond_clause
	'''
	if (Debug1) : print "Rule Used:114"


def p_cond_clause(p):
	'''cond_clause : cond_part statement_s
	'''
	if (Debug1) : print "Rule Used:115"


def p_cond_part(p):
	'''cond_part : condition THEN
	'''
	if (Debug1) : print "Rule Used:116"


def p_condition(p):
	'''condition : expression
	'''
	if (Debug1) : print "Rule Used:117"


def p_else_opt(p):
	'''else_opt :
	   | ELSE statement_s
	'''
	if (Debug1) : print "Rule Used:118"


def p_case_stmt(p):
	'''case_stmt : case_hdr pragma_s alternative_s END CASE ';'
	'''
	if (Debug1) : print "Rule Used:119"


def p_case_hdr(p):
	'''case_hdr : CASE expression IS
	'''
	if (Debug1) : print "Rule Used:120"


def p_alternative_s(p):
	'''alternative_s :
	   | alternative_s alternative
	'''
	if (Debug1) : print "Rule Used:121"


def p_alternative(p):
	'''alternative : WHEN choice_s ARROW statement_s
	'''
	if (Debug1) : print "Rule Used:122"


def p_loop_stmt(p):
	'''loop_stmt : label_opt iteration basic_loop id_opt ';'
	'''
	if (Debug1) : print "Rule Used:123"


def p_label_opt(p):
	'''label_opt :
	   | IDENTIFIER ':'
	'''
	if (Debug1) : print "Rule Used:124"


def p_iteration(p):
	'''iteration :
	   | WHILE condition
	   | iter_part reverse_opt discrete_range
	'''
	if (Debug1) : print "Rule Used:125"


def p_iter_part(p):
	'''iter_part : FOR IDENTIFIER IN
	'''
	if (Debug1) : print "Rule Used:126"


def p_reverse_opt(p):
	'''reverse_opt :
	   | REVERSE
	'''
	if (Debug1) : print "Rule Used:127"


def p_basic_loop(p):
	'''basic_loop : LOOP statement_s END LOOP
	'''
	if (Debug1) : print "Rule Used:128"


def p_id_opt(p):
	'''id_opt :
	   | designator
	'''
	if (Debug1) : print "Rule Used:129"


def p_block(p):
	'''block : label_opt block_decl block_body END id_opt ';'
	'''
	if (Debug1) : print "Rule Used:130"


def p_block_decl(p):
	'''block_decl :
	   | DECLARE decl_part
	'''
	if (Debug1) : print "Rule Used:131"


def p_block_body(p):
	'''block_body : BEGIN handled_stmt_s
	'''
	if (Debug1) : print "Rule Used:132"


def p_handled_stmt_s(p):
	'''handled_stmt_s : statement_s except_handler_part_opt 
	'''
	if (Debug1) : print "Rule Used:133"


def p_except_handler_part_opt(p):
	'''except_handler_part_opt :
	   | except_handler_part
	'''
	if (Debug1) : print "Rule Used:134"


def p_exit_stmt(p):
	'''exit_stmt : EXIT name_opt when_opt ';'
	'''
	if (Debug1) : print "Rule Used:135"


def p_name_opt(p):
	'''name_opt :
	   | name
	'''
	if (Debug1) : print "Rule Used:136"


def p_when_opt(p):
	'''when_opt :
	   | WHEN condition
	'''
	if (Debug1) : print "Rule Used:137"


def p_return_stmt(p):
	'''return_stmt : RETURN ';'
	   | RETURN expression ';'
	'''
	if (Debug1) : print "Rule Used:138"


def p_goto_stmt(p):
	'''goto_stmt : GOTO name ';'
	'''
	if (Debug1) : print "Rule Used:139"


def p_subprog_decl(p):
	'''subprog_decl : subprog_spec ';'
	   | generic_subp_inst ';'
	   | subprog_spec_is_push ABSTRACT ';'
	'''
	if (Debug1) : print "Rule Used:140"


def p_subprog_spec(p):
	'''subprog_spec : PROCEDURE compound_name formal_part_opt
	   | FUNCTION designator formal_part_opt RETURN name
	   | FUNCTION designator
	'''
	if (Debug1) : print "Rule Used:141"


def p_designator(p):
	'''designator : compound_name
	   | STRING
	'''
	if (Debug1) : print "Rule Used:142"


def p_formal_part_opt(p):
	'''formal_part_opt : 
	   | formal_part
	'''
	if (Debug1) : print "Rule Used:143"


def p_formal_part(p):
	'''formal_part : '(' param_s ')'
	'''
	if (Debug1) : print "Rule Used:144"


def p_param_s(p):
	'''param_s : param
	   | param_s ';' param
	'''
	if (Debug1) : print "Rule Used:145"


def p_param(p):
	'''param : def_id_s ':' mode mark init_opt
	   | error
	'''
	if (Debug1) : print "Rule Used:146"


def p_mode(p):
	'''mode :
	   | IN
	   | OUT
	   | IN OUT
	   | ACCESS
	'''
	if (Debug1) : print "Rule Used:147"


def p_subprog_spec_is_push(p):
	'''subprog_spec_is_push : subprog_spec IS
	'''
	if (Debug1) : print "Rule Used:148"


def p_subprog_body(p):
	'''subprog_body : subprog_spec_is_push decl_part block_body END id_opt ';'
	'''
	if (Debug1) : print "Rule Used:149"


def p_procedure_call(p):
	'''procedure_call : name ';'
	'''
	if (Debug1) : print "Rule Used:150"


def p_pkg_decl(p):
	'''pkg_decl : pkg_spec ';'
	   | generic_pkg_inst ';'
	'''
	if (Debug1) : print "Rule Used:151"


def p_pkg_spec(p):
	'''pkg_spec : PACKAGE compound_name IS decl_item_s private_part END c_id_opt
	'''
	if (Debug1) : print "Rule Used:152"


def p_private_part(p):
	'''private_part :
	   | PRIVATE decl_item_s
	'''
	if (Debug1) : print "Rule Used:153"


def p_c_id_opt(p):
	'''c_id_opt : 
	   | compound_name
	'''
	if (Debug1) : print "Rule Used:154"


def p_pkg_body(p):
	'''pkg_body : PACKAGE BODY compound_name IS decl_part body_opt END c_id_opt ';'
	'''
	if (Debug1) : print "Rule Used:155"


def p_body_opt(p):
	'''body_opt :
	   | block_body
	'''
	if (Debug1) : print "Rule Used:156"


def p_private_type(p):
	'''private_type : tagged_opt limited_opt PRIVATE
	'''
	if (Debug1) : print "Rule Used:157"


def p_limited_opt(p):
	'''limited_opt :
	   | LIMITED
	'''
	if (Debug1) : print "Rule Used:158"


def p_use_clause(p):
	'''use_clause : USE name_s ';'
	   | USE TYPE name_s ';'
	'''
	if (Debug1) : print "Rule Used:159"


def p_name_s(p):
	'''name_s : name
	   | name_s ',' name
	'''
	if (Debug1) : print "Rule Used:160"


def p_rename_decl(p):
	'''rename_decl : def_id_s ':' object_qualifier_opt subtype_ind renames ';'
	   | def_id_s ':' EXCEPTION renames ';'
	   | rename_unit
	'''
	if (Debug1) : print "Rule Used:161"


def p_rename_unit(p):
	'''rename_unit : PACKAGE compound_name renames ';'
	   | subprog_spec renames ';'
	   | generic_formal_part PACKAGE compound_name renames ';'
	   | generic_formal_part subprog_spec renames ';'
	'''
	if (Debug1) : print "Rule Used:162"


def p_renames(p):
	'''renames : RENAMES name
	'''
	if (Debug1) : print "Rule Used:163"


def p_task_decl(p):
	'''task_decl : task_spec ';'
	'''
	if (Debug1) : print "Rule Used:164"


def p_task_spec(p):
	'''task_spec : TASK simple_name task_def
	   | TASK TYPE simple_name discrim_part_opt task_def
	'''
	if (Debug1) : print "Rule Used:165"


def p_task_def(p):
	'''task_def :
	   | IS entry_decl_s rep_spec_s task_private_opt END id_opt
	'''
	if (Debug1) : print "Rule Used:166"


def p_task_private_opt(p):
	'''task_private_opt :
	   | PRIVATE entry_decl_s rep_spec_s
	'''
	if (Debug1) : print "Rule Used:167"


def p_task_body(p):
	'''task_body : TASK BODY simple_name IS decl_part block_body END id_opt ';'
	'''
	if (Debug1) : print "Rule Used:168"


def p_prot_decl(p):
	'''prot_decl : prot_spec ';'
	'''
	if (Debug1) : print "Rule Used:169"


def p_prot_spec(p):
	'''prot_spec : PROTECTED IDENTIFIER prot_def
	   | PROTECTED TYPE simple_name discrim_part_opt prot_def
	'''
	if (Debug1) : print "Rule Used:170"


def p_prot_def(p):
	'''prot_def : IS prot_op_decl_s prot_private_opt END id_opt
	'''
	if (Debug1) : print "Rule Used:171"


def p_prot_private_opt(p):
	'''prot_private_opt :
	   | PRIVATE prot_elem_decl_s 
	'''
	if (Debug1) : print "Rule Used:172"


def p_prot_op_decl_s(p):
	'''prot_op_decl_s : 
	   | prot_op_decl_s prot_op_decl
	'''
	if (Debug1) : print "Rule Used:173"


def p_prot_op_decl(p):
	'''prot_op_decl : entry_decl
	   | subprog_spec ';'
	   | rep_spec
	   | pragma
	'''
	if (Debug1) : print "Rule Used:174"


def p_prot_elem_decl_s(p):
	'''prot_elem_decl_s : 
	   | prot_elem_decl_s prot_elem_decl
	'''
	if (Debug1) : print "Rule Used:175"


def p_prot_elem_decl(p):
	'''prot_elem_decl : prot_op_decl 
    | comp_decl
	'''
	if (Debug1) : print "Rule Used:176"


def p_prot_body(p):
	'''prot_body : PROTECTED BODY simple_name IS prot_op_body_s END id_opt ';'
	'''
	if (Debug1) : print "Rule Used:177"


def p_prot_op_body_s(p):
	'''prot_op_body_s : pragma_s
	   | prot_op_body_s prot_op_body pragma_s
	'''
	if (Debug1) : print "Rule Used:178"


def p_prot_op_body(p):
	'''prot_op_body : entry_body
	   | subprog_body
	   | subprog_spec ';'
	'''
	if (Debug1) : print "Rule Used:179"


def p_entry_decl_s(p):
	'''entry_decl_s : pragma_s
	   | entry_decl_s entry_decl pragma_s
	'''
	if (Debug1) : print "Rule Used:180"


def p_entry_decl(p):
	'''entry_decl : ENTRY IDENTIFIER formal_part_opt ';'
	   | ENTRY IDENTIFIER '(' discrete_range ')' formal_part_opt ';'
	'''
	if (Debug1) : print "Rule Used:181"


def p_entry_body(p):
	'''entry_body : ENTRY IDENTIFIER formal_part_opt WHEN condition entry_body_part
	   | ENTRY IDENTIFIER '(' iter_part discrete_range ')' formal_part_opt WHEN condition entry_body_part
	'''
	if (Debug1) : print "Rule Used:182"


def p_entry_body_part(p):
	'''entry_body_part : ';'
	   | IS decl_part block_body END id_opt ';'
	'''
	if (Debug1) : print "Rule Used:183"


def p_rep_spec_s(p):
	'''rep_spec_s :
	   | rep_spec_s rep_spec pragma_s
	'''
	if (Debug1) : print "Rule Used:184"


def p_entry_call(p):
	'''entry_call : procedure_call
	'''
	if (Debug1) : print "Rule Used:185"


def p_accept_stmt(p):
	'''accept_stmt : accept_hdr ';'
	   | accept_hdr DO handled_stmt_s END id_opt ';'
	'''
	if (Debug1) : print "Rule Used:186"


def p_accept_hdr(p):
	'''accept_hdr : ACCEPT entry_name formal_part_opt
	'''
	if (Debug1) : print "Rule Used:187"


def p_entry_name(p):
	'''entry_name : simple_name
	   | entry_name '(' expression ')'
	'''
	if (Debug1) : print "Rule Used:188"


def p_delay_stmt(p):
	'''delay_stmt : DELAY expression ';'
	   | DELAY UNTIL expression ';'
	'''
	if (Debug1) : print "Rule Used:189"


def p_select_stmt(p):
	'''select_stmt : select_wait
	   | async_select
	   | timed_entry_call
	   | cond_entry_call
	'''
	if (Debug1) : print "Rule Used:190"


def p_select_wait(p):
	'''select_wait : SELECT guarded_select_alt or_select else_opt  END SELECT ';'
	'''
	if (Debug1) : print "Rule Used:191"


def p_guarded_select_alt(p):
	'''guarded_select_alt : select_alt
	   | WHEN condition ARROW select_alt
	'''
	if (Debug1) : print "Rule Used:192"


def p_or_select(p):
	'''or_select :
	   | or_select OR guarded_select_alt
	'''
	if (Debug1) : print "Rule Used:193"


def p_select_alt(p):
	'''select_alt : accept_stmt stmts_opt
	   | delay_stmt stmts_opt
	   | TERMINATE ';'
	'''
	if (Debug1) : print "Rule Used:194"


def p_delay_or_entry_alt(p):
	'''delay_or_entry_alt : delay_stmt stmts_opt
	   | entry_call stmts_opt
	'''
	if (Debug1) : print "Rule Used:195"


def p_async_select(p):
	'''async_select : SELECT delay_or_entry_alt THEN ABORT statement_s END SELECT ';'
	'''
	if (Debug1) : print "Rule Used:196"


def p_timed_entry_call(p):
	'''timed_entry_call : SELECT entry_call stmts_opt OR delay_stmt stmts_opt END SELECT ';'
	'''
	if (Debug1) : print "Rule Used:197"


def p_cond_entry_call(p):
	'''cond_entry_call : SELECT entry_call stmts_opt ELSE statement_s END SELECT ';'
	'''
	if (Debug1) : print "Rule Used:198"


def p_stmts_opt(p):
	'''stmts_opt :
	   | statement_s
	'''
	if (Debug1) : print "Rule Used:199"


def p_abort_stmt(p):
	'''abort_stmt : ABORT name_s ';'
	'''
	if (Debug1) : print "Rule Used:200"


def p_compilation(p):
	'''compilation :
	   | compilation comp_unit
	   | pragma pragma_s
	'''
	if (Debug1) : print "Rule Used:201"


def p_comp_unit(p):
	'''comp_unit : context_spec private_opt unit pragma_s
	   | private_opt unit pragma_s
	'''
	if (Debug1) : print "Rule Used:202"


def p_private_opt(p):
	'''private_opt :
	   | PRIVATE
	'''
	if (Debug1) : print "Rule Used:203"


def p_context_spec(p):
	'''context_spec : with_clause use_clause_opt
	   | context_spec with_clause use_clause_opt
	   | context_spec pragma
	'''
	if (Debug1) : print "Rule Used:204"


def p_with_clause(p):
	'''with_clause : WITH c_name_list ';'
	'''
	if (Debug1) : print "Rule Used:205"


def p_use_clause_opt(p):
	'''use_clause_opt :
	   | use_clause_opt use_clause
	'''
	if (Debug1) : print "Rule Used:206"


def p_unit(p):
	'''unit : pkg_decl
	   | pkg_body
	   | subprog_decl
	   | subprog_body
	   | subunit
	   | generic_decl
	   | rename_unit
	'''
	if (Debug1) : print "Rule Used:207"


def p_subunit(p):
	'''subunit : SEPARATE '(' compound_name ')' subunit_body
	'''
	if (Debug1) : print "Rule Used:208"


def p_subunit_body(p):
	'''subunit_body : subprog_body
	   | pkg_body
	   | task_body
	   | prot_body
	'''
	if (Debug1) : print "Rule Used:209"


def p_body_stub(p):
	'''body_stub : TASK BODY simple_name IS SEPARATE ';'
	   | PACKAGE BODY compound_name IS SEPARATE ';'
	   | subprog_spec IS SEPARATE ';'
	   | PROTECTED BODY simple_name IS SEPARATE ';'
	'''
	if (Debug1) : print "Rule Used:210"


def p_exception_decl(p):
	'''exception_decl : def_id_s ':' EXCEPTION ';'
	'''
	if (Debug1) : print "Rule Used:211"


def p_except_handler_part(p):
	'''except_handler_part : EXCEPTION exception_handler
	   | except_handler_part exception_handler
	'''
	if (Debug1) : print "Rule Used:212"


def p_exception_handler(p):
	'''exception_handler : WHEN except_choice_s ARROW statement_s
	   | WHEN IDENTIFIER ':' except_choice_s ARROW statement_s
	'''
	if (Debug1) : print "Rule Used:213"


def p_except_choice_s(p):
	'''except_choice_s : except_choice
	   | except_choice_s '|' except_choice
	'''
	if (Debug1) : print "Rule Used:214"


def p_except_choice(p):
	'''except_choice : name
	   | OTHERS
	'''
	if (Debug1) : print "Rule Used:215"


def p_raise_stmt(p):
	'''raise_stmt : RAISE name_opt ';'
	'''
	if (Debug1) : print "Rule Used:216"


def p_requeue_stmt(p):
	'''requeue_stmt : REQUEUE name ';'
	   | REQUEUE name WITH ABORT ';'
	'''
	if (Debug1) : print "Rule Used:217"


def p_generic_decl(p):
	'''generic_decl : generic_formal_part subprog_spec ';'
	   | generic_formal_part pkg_spec ';'
	'''
	if (Debug1) : print "Rule Used:218"


def p_generic_formal_part(p):
	'''generic_formal_part : GENERIC
	   | generic_formal_part generic_formal
	'''
	if (Debug1) : print "Rule Used:219"


def p_generic_formal(p):
	'''generic_formal : param ';'
	   | TYPE simple_name generic_discrim_part_opt IS generic_type_def ';'
	   | WITH PROCEDURE simple_name formal_part_opt subp_default ';'
	   | WITH FUNCTION designator formal_part_opt RETURN name subp_default ';'
	   | WITH PACKAGE simple_name IS NEW name '(' LESSMORE ')' ';'
	   | WITH PACKAGE simple_name IS NEW name ';'
	   | use_clause
	'''
	if (Debug1) : print "Rule Used:220"


def p_generic_discrim_part_opt(p):
	'''generic_discrim_part_opt :
	   | discrim_part
	   | '(' LESSMORE ')'
	'''
	if (Debug1) : print "Rule Used:221"


def p_subp_default(p):
	'''subp_default :
	   | IS name
	   | IS LESSMORE
	'''
	if (Debug1) : print "Rule Used:222"


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
	if (Debug1) : print "Rule Used:223"


def p_generic_derived_type(p):
	'''generic_derived_type : NEW subtype_ind
	   | NEW subtype_ind WITH PRIVATE
	   | ABSTRACT NEW subtype_ind WITH PRIVATE
	'''
	if (Debug1) : print "Rule Used:224"


def p_generic_subp_inst(p):
	'''generic_subp_inst : subprog_spec IS generic_inst
	'''
	if (Debug1) : print "Rule Used:225"


def p_generic_pkg_inst(p):
	'''generic_pkg_inst : PACKAGE compound_name IS generic_inst
	'''
	if (Debug1) : print "Rule Used:226"


def p_generic_inst(p):
	'''generic_inst : NEW name
	'''
	if (Debug1) : print "Rule Used:227"


def p_rep_spec(p):
	'''rep_spec : attrib_def
	   | record_type_spec
	   | address_spec
	'''
	if (Debug1) : print "Rule Used:228"


def p_attrib_def(p):
	'''attrib_def : FOR mark USE expression ';'
	'''
	if (Debug1) : print "Rule Used:229"


def p_record_type_spec(p):
	'''record_type_spec : FOR mark USE RECORD align_opt comp_loc_s END RECORD ';'
	'''
	if (Debug1) : print "Rule Used:230"


def p_align_opt(p):
	'''align_opt :
	   | AT MOD expression ';'
	'''
	if (Debug1) : print "Rule Used:231"


def p_comp_loc_s(p):
	'''comp_loc_s :
	   | comp_loc_s mark AT expression RANGE range ';'
	'''
	if (Debug1) : print "Rule Used:232"


def p_address_spec(p):
	'''address_spec : FOR mark USE AT expression ';'
	'''
	if (Debug1) : print "Rule Used:233"


def p_code_stmt(p):
	'''code_stmt : qualified ';'
	'''
	if (Debug1) : print "Rule Used:234"
