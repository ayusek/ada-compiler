with Ada.Text_IO;
with Ada.Command_Line;
with Ada.Strings.Bounded;

procedure Show_Commandline_3 is

   package T_IO renames Ada.Text_IO;
   package CL   renames Ada.Command_Line;

   function Max_Length (
      Value_1 : Integer;
      Value_2 : Integer)
   return
      Integer
   is
      Retval : Integer;
   begin
      if Value_1 > Value_2 then
         Retval := Value_1;
      else
         Retval := Value_2;
      end if;
      return Retval;
   end Max_Length;

   pragma Inline (Max_Length);

   package SB
   is new Ada.Strings.Bounded.Generic_Bounded_Length (
       Max => Max_Length (
                  Value_2 => CL.Argument (1)'Length,
                  Value_1 => CL.Argument (2)'Length));

   X :  SB.Bounded_String
     := SB.To_Bounded_String (CL.Argument (1));

begin
   T_IO.Put ("Argument 1 = ");
   T_IO.Put_Line (SB.To_String (X));

   X := SB.To_Bounded_String (CL.Argument (2));

   T_IO.Put ("Argument 2 = ");
   T_IO.Put_Line (SB.To_String (X));
end Show_Commandline_3;
