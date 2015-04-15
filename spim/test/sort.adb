-- insertion sort

 
procedure sort  is

   A : Array (1 .. 10) of Integer;
   Value : Integer;
   J : integer;

begin

   Print_char('G', 'i', 'v', 'e', ' ', '1', '0', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's', ' ', 'a', 's', ' ', 'i', 'n', 'p', 'u', 't');
   Print_newline(1);

   for m in 1 .. 10 loop 
      Scan_int(A(m));
   end loop;

   for I in 1 .. 10 loop

      Value := A(I);
      J := I - 1;

      while J >= 0 and then A(J) > Value loop
         A(J + 1) := A(J);
         J := J - 1;
      end loop;
      A(J + 1) := Value;
   end loop; 

   Print_char('S', 'o', 'r', 't', 'e', 'd', ' ', 'a', 'r', 'r', 'a', 'y', ' ', 'i', 's', ':');
   Print_newline(1);
   for n in 1 .. 10 loop 
      Print_int(A(n));
      Print_newline(1);
   end loop;

end sort;
