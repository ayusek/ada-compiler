-- arrays and Types and range types

with Ada.Text_IO;
use Ada.Text_IO;

procedure test5 is
      a,b,c : integer := 1;  
      type I is range 1 .. 7; -- range type declaration and usage
      type AC is array (1 .. 7) of integer ; 
      type AC2 is array (1 .. 7) of integer ; 
      type ACC is array (1 .. 7 , 1 .. 7 ) of integer ; 

      hello : AC ;
      hello1 : ACC;
      hello2 : array(1 .. 7 , 1 .. 7) of integer ; 

      d : I ; -- d is a range

begin

   a := 1; 

   for m in I  loop
   hello1(m,m) := m;
   hello2(m,m) := m;
   end loop;

   --Testing a range
   For_Loop1 :
     for j in reverse I  loop

      Print_int(hello1(j,j));
      Print_int(hello2(j, j));

      Print_newline(1);

     end loop For_Loop1;

end test5;
