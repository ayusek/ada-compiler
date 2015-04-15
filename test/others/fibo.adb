with Ada.Text_IO;
use Ada.Text_IO;

procedure fibo is
a, d , b : integer := 1;


procedure eq1(a: in integer := 1 ; d: out integer ) is
		i , j : integer := 1 ; 

        begin
        if ( a = 1) then

        	d := 1; 

        elsif ( a = 2) then 

        	d := 1; 

        else

        	eq1(a-1 , i);
        	eq1(a-2 , j);
        	d := i + j ; 

        end if;
        end eq1;
begin

	eq1(6 , b);
	Print_int(b);
	Print_newline(1);

end fibo;