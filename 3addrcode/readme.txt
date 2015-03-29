Symbol Table:
We have not yet added the function overloading feature to out language. 

Ranges : 
Ranges are specifies as expression .. expression

operators:
The two types must be same on the two sides of the operators


Stuff Handled:
Variable Declaration
Expression Declaration
Type Declaration 
Procedure Declaration
Statement Declaration

Temperory variables:
Their lexemes are of the format of t. where . is a number 

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


Emit_codes Types : 
emit(temp, None , "un-" , operand)
emit(temp , p[1]["value"] , p[2] , p[3]["value"])  #p[2] = + , - , & 
emit(temp ,p[1]["value"],"dotdot" , p[3]["value"])
three_addr_code.emit("goto", p[1]["value"] , p[2] ,   p[3]["value"])
three_addr_code.emit("goto" , None , None , None)
three_addr_code.emit("blteq" , p[2]["value"] , p[3]["upper_limit"] , None)