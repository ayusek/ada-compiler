-- arrays and Types

with Ada.Text_IO;
use Ada.Text_IO;

procedure arrays is
      a,b,c : integer := 1;  
      type I is range 1 .. 10; -- range type declaration and usage
      type AC is array (1 .. 10) of integer ; 
      type ACC is array (1 .. 10 , 2 .. 8 ) of integer ; 

      hello : AC ;
      hello1 : ACC;
      hello2 : array(1 .. 7 , 2..8) of integer ; 

      d : I ; -- d is a range

begin

   a := 1; 

   --Testing a range
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
   hello2(1,3) := 3; 
   hello2(a + 1 , a) := hello2(a,a) + 1 ; 
   --hello(1);

end arrays;
