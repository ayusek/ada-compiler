 --File explaining all the ada tokens
 with Ada.Text_IO, Ada.Integer_Text_IO , Ada.Float_text_IO, Ada.Command_Line;
 use Ada.Text_IO , Ada.Float_text_IO, Ada.Integer_Text_IO ;
 use Ada;
 

 procedure Simple is
    A:Integer;
    B:Float;
    C:string := "Hello, World";
    D:Character;
 begin

    --Some initializations for lexer demo
    A := 2; -- Normal Integer
    A := 2_2; --  Normal Integer with _
    A := 2E2; -- Integer with expoenents
    A := 2#101#; -- Universal Integer
    A := 16#B#E2; -- universal Integer with Exponent
    B := 1.1; -- Normal Float
    B := 1_1.23_4 ; -- Normal Float with _
    B := 1.1E2 ; -- Normal Float with Expoenent
    B := 1.1E-2 ; -- Normal Float with Negative Exponent
    B := 1.1E+2 ; -- Normal Float with + in Exponent
    B := 9#7.801#E2; -- Universal Float with Exponent
    B := 16#BA.0#E-2; -- Univeral Float with negative exponent
    D := 'a'; -- Character

    put("Give an Integer in normal or exponential form (You can use _ as a separtor and can use base_Integers  as well): ");
    get(item => A); 
    put("Integer Given is: ");put(A , width=>0);
    new_line(1);
    
    put("Give a Float in decimal or exponential form: (Use _ as a separator and can use base_Floats as well)");
    get(item => B);
    put("Float Given is: ");put(Float'Image(B));
    new_line(1);
    put_line(C);
    put_line(character'Image(D));
 end Simple;
