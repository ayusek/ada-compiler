with Ada.Text_IO;
use Ada.Text_IO;

procedure Flushtest is
str : String (1..10);
i : Natural := 1; 
begin
   Put_Line ("Type anything for 2 s");
   delay 2.0;
--Does not scans the stuff.. 
Flush_Input:
   declare
      Ch   : Character;
      More : Boolean;
   begin
      loop
         Get_Immediate (str(i..i), More);
	i := i + 1;
         exit when not More;
      end loop;
   end Flush_Input;
   New_Line;
   Put_Line(i);
  New_Line;
   Put_Line ("Okay, thanks. Here is some input from you:");
   Put_Line (Get_Line);
end Flushtest;
