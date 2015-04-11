with Ada.Text_IO;
use Ada.Text_IO;

procedure Proced1 is
a,b,c : integer := 1; 

begin

-- if else if

    b := 2;
    if ( a >= 10) then
    b := 2;
  elsif (a >= 0) then 
    b := 1 ; 
  else
    b := 4; 
    end if ; 


-- Nested if's
  if ((c = 1) and (b = 2) or (c /= 1)) then
        a := 1;
        if(a >= 1) then 
        a := 10;
        end if ; 
      else
        a := 2 ; 
        end if; 

-- While loop 

  While_Loop :
     while a <= 5 loop

      if c = 1 then
        a := 1 ;
      else
        a := 2 ; 
        end if ; 

        a := 1 ;

     end loop While_Loop;

-- Infinite While loop
  While_Loop1 :
     loop

          if c = 1 then
        a := 1 ;
      else
        a := 2 ; 
        end if ; 

        b := 1 ; 

     end loop While_Loop1;

-- For each loop 
   For_Loop :
     for i in  1 .. 10  loop

          if c = 1 then
        a := 1;
      else
        a := 2 ; 
        end if ; 
        
        c := 1;

     end loop For_Loop;


-- For each reverse loop 
   For_Loop1 :
     for j in reverse 10 .. 1 loop

          if c = 1 then
        a := 1;
      else
        a := 2 ; 
        end if ; 
        
        c := 1;

     end loop For_Loop1;


end Proced1;
