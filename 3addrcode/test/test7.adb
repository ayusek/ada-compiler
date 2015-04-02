with Ada.Text_IO;
use Ada.Text_IO;

procedure arrays is
a,b,c : integer := 1;  
type I is range 1 .. 10; 
Dummy1 : array(1 .. 7 , 2..8) of integer;
d : integer := 1; 
type AC is array (1 .. 10) of integer; 
hello : AC ; 

begin
   a := 1; 

   for iter in I loop
    a := 2;
    end loop ; 

    While_Loop1 :
     loop

          if c = 1 then
        a := 1 ;
      else
        a := 2 ; 
        end if ; 

        b := 1 ; 

     end loop While_Loop1;

end arrays;