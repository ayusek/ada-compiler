with Ada.Text_IO;
use Ada.Text_IO;

procedure nesting is
   a,b : integer := 1; 

   procedure Triple(a:in  integer) is
         procedure Second_Layer(a:in integer) is
               procedure Bottom_Layer(a: in integer) is
               begin
                  Print_char('b');
                  a := 5;  
                  Print_char('b');
               end Bottom_Layer;
         begin
            Print_char('s');
            a := 2;
            Bottom_Layer(a);
            Print_char('s');

         end Second_Layer;

   begin
      Print_char('t');
      a := 3;
      b := 1; 
      Second_Layer(b);
      --Bottom_Layer(a);
      Print_int(b);
      Print_int(a);
      Print_char('t');
   end Triple;

begin

   Triple(a);

end nesting;
