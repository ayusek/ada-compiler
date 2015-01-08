with Ada.Text_IO;
 
procedure Main is
  Str1  : String (1..3);
  Str2 : String (1..4);
  Last : Natural;
begin
  Ada.Text_IO.Get_Line (Str1, Last);
  Ada.Text_IO.Put_Line (Str1 (1..Last)); 
 Flush;
  Ada.Text_IO.Get_Line (Str2, Last);
  Ada.Text_IO.Put_Line (Str2 (1..Last));
end;
