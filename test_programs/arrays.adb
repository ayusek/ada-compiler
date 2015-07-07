with Ada.Text_IO;
use Ada.Text_IO;

procedure arrays is
a,b : integer := 1;  
Dummy1 : array(2 .. 7 , 3..8 , 1 .. 9) of integer ;
d : integer := 1 ; 

begin

	a := 3; 
	b := a;
	d := b;
	Print_int(d);

end arrays;