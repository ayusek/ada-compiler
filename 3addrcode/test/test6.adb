                                       -- Chapter 8 - Program 1
with Ada.Text_IO;
use Ada.Text_IO;

procedure Proced1 is

      procedure Write_A_Line is
      begin
         Put("This is a line of text.");
         New_Line;
      end Write_A_Line;

begin
   Write_A_Line;
   Write_A_Line;
end Proced1;

