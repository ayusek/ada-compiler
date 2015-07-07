procedure string is

   a : integer := 0 ;
   str : array (1 .. 100) of character;
begin
   Scan_int(a);

   for i in 1 .. a loop
      Scan_char(str(i));
   end loop;

   Print_newline(1);

   for j in 1 .. a loop
      Print_char(str(j));
   end loop;

   Print_newline(1);
   
end string;