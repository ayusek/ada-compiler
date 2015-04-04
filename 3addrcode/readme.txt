Operators: 
Distinction has been made between the Int and Float type operators, Unless specified , the operators are Int based

Types  Handles:
I have handled only Int, Float and char types.
Not all operations are handled on the char types

Loops :
We have handled loops on ranges, range objects as well as range types
Break and continue do not exists for Ada loops

Expressions :
All algebric expressions are handled. 
While having nested booleans, some temperory variables are emitted but are not used.
Only short circuit operators are allowed "and then" and "or else"


Procedures and Functions : 
I have only defined procedures, support to functions is not yet handled. 
Expressions are only allowed for in parameters
Write now, I have handled only in and out variables, so procedure variables are used only to transfer values only. 
I have not yet put any constraints on their assignments
Right now, I have also not handled the default value assignment to procedures. This is to be done in p_comp_assoc 
Also, the offset in each procedure is a local offset in its activation record. 

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

Not Handled: 
Pragma's - They are compiler derivatives, I was not able to understand them

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

Symbol table not yet introduced


Statement Types :
Empty statements are not allowed

Loops :
Loop identifiers can not be used again
Did not deal with until loops and loops with conditions in the middle
Array Loops are not defined for now
Assume loop variables to be global identifiers

Blocks:
Exceptions not handled yet

Emit_codes Types : 
emit(temp, None , "un-" , operand)
emit(temp , p[1]["value"] , p[2] , p[3]["value"])  #p[2] = + , - , & 
emit(temp ,p[1]["value"],"dotdot" , p[3]["value"])
three_addr_code.emit("goto", p[1]["value"] , p[2] ,   p[3]["value"])
three_addr_code.emit("goto" , None , None , None)
three_addr_code.emit("blteq" , p[2]["value"] , p[3]["upper_limit"] , None)
three_addr_code.emit("proc_label" , p[1]["lexeme"] ,None , None )