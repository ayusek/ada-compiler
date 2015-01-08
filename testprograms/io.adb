with Ada.Text_IO;
use Ada.Text_IO;
with Ada.Integer_text_IO;
procedure Main is
  Str  : String (1..5);
  Last : Natural;  
  Strd : String (1..5);
begin
 Ada.Text_IO.Get_Line(Str(2..1) , Last );
 Strd(1..3) := Str(1..3);
 Ada.Text_IO.Put_Line (strd);
 Ada.Integer_text_IO.put(Last);
end;
