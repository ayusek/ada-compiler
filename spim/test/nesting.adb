with Ada.Text_IO;
use Ada.Text_IO;

procedure test7 is
   a : integer ; 

   procedure Triple(a:out integer) is
         procedure Second_Layer(a:out integer) is
               procedure Bottom_Layer(a: out integer) is
               begin
                  Print_char('b');
                  a := 1;  
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
      Second_Layer(a);
      Print_char('t');
   end Triple;

begin

   Triple(a);

end test7;
