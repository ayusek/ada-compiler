 -- mult.adb: program with matrix multiplication subprocedure
 
 procedure Mult is
 
    type Matrix is array (1 .. 10 , 1 .. 10) of Integer;
 
    A,B: Matrix ;
    C: Matrix;

    -- Matrix multiplication
    procedure Multiply (A,B: in Matrix; C: out Matrix) is
    Sum : Integer := 1; 
    begin
 
 
       for Row in 1 .. 10  loop
          for Col in 1 .. 10 loop
             begin
                for I in 1 .. 10  loop
                   Sum := Sum + A(Row,I)*B(I,Col);
                end loop;
                C(Row,Col) := Sum;
             end;
          end loop;
       end loop;
    end Multiply;
 
 begin
    A(1,1) := 1;
    --Multiply (A,B,C);
    --Multiply (A,B,A);  -- does not work as expected.
 
 end Mult;
