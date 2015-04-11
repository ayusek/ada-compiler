 -- nonzero.adb:  find last nonzero digit of N factorial
 
 with Ada.Text_IO, Ada.Integer_Text_IO;
 use Ada;
 
 procedure Nonzero is
 
    N , Twos : Natural;
    P , J : Positive;
 
 begin
 
    while not (Text_IO.End_Of_File) loop -- Using end of file 
 
       Integer_Text_IO.Get (N);
       P := 1;  Twos := 0;
 
       for I in 2..N loop
 
          -- discard factors of 2 and 5 from I
          J := I;
          while J mod 2 = 0 loop J := J / 2; Twos := Twos + 1; end loop;
          while J mod 5 = 0 loop J := J / 5; Twos := Twos - 1; end loop;
 
          -- compute the last digit of the factorial of I without
          -- any factors of 2 or 5 included
          P := (J*P) mod 10;
 
       end loop;
 
       -- restore factors of 2 excepted those canceled by a 5
       for I in 1..Twos loop P := (2*P) mod 10; end loop;
 
       Integer_Text_IO.Put (N, Width=>5);
       Text_IO.Put (" ->");
       Integer_Text_IO.Put (P, Width=>1);
       Text_IO.New_Line;
 
    end loop;
 
 end Nonzero;
