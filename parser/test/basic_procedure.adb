with Ada.Text_IO;
use Ada.Text_IO;

procedure Proced1 is
a,b,c : integer := 1; 

procedure eq1(a , b: in integer := 1 ; d: out integer ) is
            i: integer := 1;
        begin
            d := a ; 
        end eq1;

begin

 a := 1; 
 b := 1; 

 eq1(a + 1,b,c);


end Proced1;