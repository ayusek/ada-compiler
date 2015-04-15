with Ada.Text_Io; use Ada.Text_Io;
 
procedure towers is
   a : integer ;
   procedure Hanoi (Ndisks, Start_Peg, End_Peg, Via_Peg : in integer) is

   begin

      if Ndisks > 0 then
         Hanoi(Ndisks - 1, Start_Peg, Via_Peg, End_Peg);

         Print_int(Ndisks);
         Print_char(' ', ':', ' ');
         Print_int(Start_Peg);
         Print_char(' ','-','>',' ');
         Print_int(End_Peg);
         Print_newline(1);

         Hanoi(Ndisks - 1, Via_Peg, End_Peg, Start_Peg);
      end if;

   end Hanoi;

begin
   --Print_string( "hello" );
   Scan_int(a);
   Hanoi(a , 0 , 2 , 1);

end towers;