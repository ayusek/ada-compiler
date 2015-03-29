with Ada.Text_IO;
use Ada.Text_IO;

procedure Proced1 is
a,b : float := 1.1;
c:integer := 1; 
begin

c := 2; 


For_Loop :
   for i in reverse 10 .. 1 loop

   			if c = 1 then
      a := 1.9 ;
    else
      a := 2.0 ; 
      end if ; 
      
      c := 1;

   end loop For_Loop;


While_Loop1 :
   loop

   			if c = 1 then
      a := 1.9 ;
    else
      a := 2.0 ; 
      end if ; 

      b := 1.6 ; 

   end loop While_Loop1;


While_Loop :
   while a <= 5.0 loop

   	if c = 1 then
      a := 1.9 ;
    else
      a := 2.0 ; 
      end if ; 

      a := 1.0 ;

   end loop While_Loop;

b := 0.0 ; 
end Proced1;