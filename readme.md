#				Ada Compiler
###			Ayush Sekhari (ayusek@iitk.ac.in) , Margaux Dorido (margaux.dorido@gmail.com)

This is a simplified compiler for converting an **Ada Program to MIPS assembly code** which can be directly simulated on a SPIM.  This was build under the supervision of **Prof. Subhajit Roy** as a course project for the course Compiler Design (CS335A) at IIT Kanpur. 

The Project was made in four sub-parts :

1. **Lexer** - Returns the lexemes for the input Ada code
2. **Parser** - Returns a Parse Tree for the input Ada code by first running the above lexer to get the lexemes for each token
3. **IRCode Generator** - Returns a List of Three Adress Code for the input Ada code using a CFL for a part of Ada. 
4. **Spim code Generator** - Returns the assembly code for the given input Ada code which can be directly executed on SPIM. 

-------------------------------------------------------------------------------------------------------
For running the compiler just execute the respective part\_file.py with the code file as an argument. Eq  ./spimgen/spimgen.py  test_file.adb

-------------------------------------------------------------------------------------------------------
### Language Features
#### Basic Data-Types :
Int, Float and char data types. Not all operations are handled on the char types. Basic level string handling is done. 

####Arrays: 
1. I am assuming an integral range only. No need to specify the type of range while initiating arrays.
2. The size of arrays is to be fixed at compile_time.  Dynamic arrays are not supported. 


#### Ranges : 
1. Ranges are specifies as expression .. expression
2. Only numerical ranges are allowed
3. Reverse keyword can be used to invert the range specification

####Operators: 

1. Distinction has been made between the Int and Float type operators
2. Power Operator (**). It works on integers only
3 .Unary + and - have also been supported

#### Expressions :
1. All algebric expressions  are handled. 
2. All boolean operators are short circuit operators i.e. "and then" and "or else"
3. Xor boolean operator is not supported

#### Loops :

1.  We have handled loops on ranges, range objects as well as range types
2. Break and continue statements are supported
3. Loop identifiers must not be used again in the code
4. While loop and For loop have been supported

####Procedures and Functions : 
1. A maximum of two  integral/character  and five floating point return values are allowed in procedures 
2. I have only defined procedures, support to functions is not yet handled. 
3. Only expressions are allowed in parameters. Objects can not be passed by direct reference.  I have handled only in and out variables, so procedure variables are used only to transfer values only. 
4. Default values in procedures have been handled. 

 #### Register Allocation :
 Trivial register allocation is done considering each three adress code statement as a basic block. 

#### Memory Allocation : 
 Instead of alocating a complete memory and making offsets in it, Right now, I am just making a new space for each variable. 
 If values are not pre-assigned, then it would take garbage values

 #### Library Support :
The following basic functions have been handled - 

 * Print_int
* Print_float
* Print_char 
* int\_to\_float
* float\_to\_int
* Scan_int
* Scan_float
* Scan_char
* Print_newline #takes number of newlines to be printed. 

#### Relevant Test Files :
* test1 -> Expressions
* test2 -> If-else, For Loop, While Loop 
* test3 -> Nested Procedures
* test4 -> Multiple Procedures
* test5 -> Arrays , Subtypes, TypeDefs
* test6 -> Passing Arrays to Functions, Matrix Type Defined

-------------------------------------------------------------------------------------------------------
