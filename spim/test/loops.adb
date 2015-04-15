
--if-else and loops

procedure loops is

a : float := -1.0 ; 

begin

   for n in 2 .. 8 loop
   Print_int(n);
   Print_newline(1);
   end loop;

   Print_newline(2);

   for m in reverse 2 .. 8 loop
   Print_int(m);
   Print_newline(1);
   end loop;

   if ( a < 0.0 ) then
      a := -a; 
      if (a > 0.0) then
         Print_float(a);
      end if ;
      a := 1.0;
   end if ; 

   Print_newline(2);

   while a < 10.0 loop
   a := a  + 0.5 ;
   Print_float(a);
   Print_newline(1);
   end loop;

   
end loops;