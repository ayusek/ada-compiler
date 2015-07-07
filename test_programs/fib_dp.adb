procedure fib_dp is
   
   a : integer := 0;
   arr : array (1 .. 100) of integer;
   ans : integer := 0; 
   
begin
   Scan_int(a);

   -- initializations
   arr(1) := 1 ;
   arr(2) := 1 ; 


   for i in 1 .. a loop
      if (i > 2) then 
         arr(i) := arr(i-1) + arr(i-2);
      end if;
   end loop;


   Print_int(arr(a));
end fib_dp;