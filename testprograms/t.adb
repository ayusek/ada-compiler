with Ada.Text_IO;

procedure Convert_Checked is
   type Short is range -128 .. +127;
   type Byte  is mod 256;

   package T_IO renames Ada.Text_IO;
   package I_IO is new Ada.Text_IO.Integer_IO (Short);
   package M_IO is new Ada.Text_IO.Modular_IO (Byte);

   A : Short := 1;
   B : Byte;
begin
   T_IO.Put("Hello");
   B := Byte (A);  -- range check will lead to Constraint_Error
   T_IO.Put ("A = ");
   I_IO.Put (Item  =>  A,
             Width =>  5,
             Base  => 10);
   T_IO.Put (", B = ");
   M_IO.Put (Item  =>  B,
             Width =>  5,
             Base  => 10);
end Convert_Checked;

