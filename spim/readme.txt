Name : Ayush Sekhari | Margaux Dorido
The following is a description of stuff I was able to handle in my implementation. 

Operators: 
Distinction has been made between the Int and Float type operators, Unless specified , the operators are Int based

Types  Handles:
I have handled only Int, Float and char types.
Not all operations are handled on the char types

Loops :
We have handled loops on ranges, range objects as well as range types
Break and continue do not exists for Ada loops
Loop identifiers can not be used again
Did not deal with until loops and loops with conditions in the middle
Array Loops are not defined for now
Assume loop variables to be global identifiers


Expressions :
All algebric expressions are handled. 
While having nested booleans, some temperory variables are emitted but are not used.
Only short circuit operators are allowed "and then" and "or else"


Procedures and Functions : 
Only two return values are allowed in procedures
I have only defined procedures, support to functions is not yet handled. 
Expressions are only allowed for in parameters
Write now, I have handled only in and out variables, so procedure variables are used only to transfer values only. 
I have not yet put any constraints on their assignments
Right now, I have also not handled the default value assignment to procedures. This is to be done in p_comp_assoc 
Also, the offset in each procedure is a local offset in its activation record. 
New defines data-types may be passed to procedures. 


Arrays: 
I am assuming an integral range only. No need to specify the type of range.
The size of arrays is to be fixed at compile_time. 
Arrays are static only. 


Types:
I have a statement type which is used for type checking in the expressions
I am handling Int, Float and Bool Data types


Symbol Table:
We have not yet added the function overloading feature to out language. 

Ranges : 
Ranges are specifies as expression .. expression
Only numerical ranges are allowed
Reverse keyword can be used to invert the range specification

operators:
The two types must be same on the two sides of the operators. ada also does not do any type casting in general. 

Stuff Handled:
Variable Declaration
Expression Declaration 
Procedure Declaration
Statement Declaration
Procedure Calling
type checking
Type/Subtype Declaration

Temperory variables:
Their lexemes are of the format of _t. where . is a number 


Logical Operators:
XOR is a logical operator in ada , I have removed it


Statement Types :
Empty statements are not allowed


Blocks:
Exceptions not handled yet

Relevant Test Files :
test1 -> Expressions
test2 -> If-else, For Loop, While Loop 
test3 -> Nested Procedures
test4 -> Multiple Procedures
test5 -> Arrays , Subtypes, TypeDefs
test6 -> Passing Arrays to Functions, Matrix Type Defined

Conversion of emitted statements to MIPS code would be handeled later on. 


 SPIM code generation :
 The filename must match the main function name or else it would give an error. This is a warning in normal ada but I am treating it as an error. 

 scoping is not handeled yet

 Memory Allocation : 
 Instead of alocating a complete memory and making offsets in it, Right now, I am just making a new space for each variable. 
 If values are not pre-assigned, then it would take garbage values

 Library Support :
 Right now, I have added the following function:

 #Takes a variable

 Print_int
 Print_float
 Print_char 

 #Takes Nothing
 Print_newline 


