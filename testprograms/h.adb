with Ada.Text_IO; 
use Ada.Text_IO;
with Ada.Integer_Text_IO;
use Ada.Integer_Text_IO;

procedure yo is 
begin
put_line("yoyo"); 
end yo;

procedure lo is
i : integer;
begin
i:= 3;
for i in 1 .. 10 loop
--   i := i + 1;
Put(i);
end loop;
end lo;

lo
