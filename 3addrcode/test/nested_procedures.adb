with Ada.Text_IO;
use Ada.Text_IO;

procedure Nesting is
   a : integer ; 
   procedure Triple(a:integer) is
         procedure Second_Layer(a:integer) is
               procedure Bottom_Layer(a:integer) is
               begin
                  a := 1;  
               end Bottom_Layer;
         begin
            a := 2;
            Bottom_Layer(a);
         end Second_Layer;

   begin
      a := 3;
      Second_Layer(a);
   end Triple;

begin
   Triple(a);
end Nesting;
