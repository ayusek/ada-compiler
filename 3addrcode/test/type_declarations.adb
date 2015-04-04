with Ada.Text_IO;
use Ada.Text_IO;

procedure arrays is
a,b,c : integer := 1;  
type I is range 1 .. 10; -- range type declaration and usage

type AC is array (1 .. 10) of integer ; 
hello : AC ; 
type ACC is array (1 .. 10 , 2 .. 8 ) of integer ; 
hello1 : ACC; 

d : I ; -- d is a range

begin

   a := 1; 

   For_Loop1 :
     for j in reverse d loop

          if c = 1 then
        a := 1;
      else
        a := 2 ; 
        end if ; 
        
        c := 1;

     end loop For_Loop1;


   hello(1) := 1; 
   hello1(1,2) := 1;
   --hello(1);

end arrays;