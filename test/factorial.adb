with Ada.Text_IO, Ada.Integer_Text_IO;
use Ada.Text_IO, Ada.Integer_Text_IO;

procedure factorial is
   n, res : integer ;
   procedure Fact(x : in Integer; result :out Integer) is

      begin
         if x>1 then
            Fact(x-1, result);
            result:=result*x;
         else
            result := x;
         end if;

      end Fact;


begin

   Scan_int(n);
   Print_int(n);
   Print_newline(1);
   Fact(n,res);
   Print_int(res);
   
end factorial;