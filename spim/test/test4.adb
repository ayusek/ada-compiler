with Ada.Text_IO;
use Ada.Text_IO;

procedure Proced1 is
a,b,c : integer := 1; 

procedure eq1(a , b: in integer := 1 ; d: out integer ) is
            i: integer := 1;
        begin
            d := a + a+  1; 
        end eq1;

procedure eq2(a , b: in integer := 1 ; d: out integer ) is
            i: integer := 1;
        begin
            d := a + a+  1; 
        end eq2;


e,f : integer := 2;

begin

 a := 1; 
 b := 1; 

 eq1(a + 1,b,c);
 eq1(a,b + 1,c);

end Proced1;