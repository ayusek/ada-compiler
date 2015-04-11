with Ada.Text_IO;
use Ada.Text_IO;

procedure test7 is
d,E,F :integer := 1; 

procedure add(a , b: in integer := 1 ; d: out integer ) is
        begin
            d := a + b*2;
            --e := a*10; 
        end add;

begin
	
	--E := (E + (F + d)*10)/7;

	add( E, F, d);
	Print_int(d);
	--Print_int(e);
	Print_newline(1);

end test7;