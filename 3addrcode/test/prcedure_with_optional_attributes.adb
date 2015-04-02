--http://www.infres.enst.fr/~pautet/Ada95/chap18.htm

                                       -- Chapter 18 - Program 1
with Ada.Text_IO, Ada.Integer_Text_IO;
use Ada.Text_IO, Ada.Integer_Text_IO;

procedure Defaults is

Index      : INTEGER;
Animal_Sum : INTEGER;

   procedure Animals(Total : in out INTEGER;
                     Cows  : in     INTEGER := 0;
                     Pigs  : in     INTEGER := 0;
                     Dogs  : in     INTEGER := 0) is
   begin
      Total := Cows + Pigs + Dogs;
      Put("Cows =");
      Put(Cows, 3);
      Put("   Pigs =");
      Put(Pigs, 3);
      Put("   Dogs =");
      Put(Dogs, 3);
      Put("   and they total");
      Put(Total, 4);
      New_Line;
   end Animals;

begin
   Index := 3;
   Animals(Animal_Sum, 2, 3, 4);
   Animals(Animal_Sum, 3, Index, 4);
   Animals(Dogs => 4, Total => Animal_Sum);
   Animals(Total => Animal_Sum, Pigs => 2 * Index + 1, Cows => 5);
   Animals(Dogs => Index + 4, Total => Animal_Sum);
   Animals(Animal_Sum, Dogs => 4, Pigs => Index, Cows => 2);
   Animals(Animal_Sum);
end Defaults;




-- Result of Execution

-- Cows =  2   Pigs =  3   Dogs =  4   and they total   9
-- Cows =  3   Pigs =  3   Dogs =  4   and they total  10
-- Cows =  0   Pigs =  0   Dogs =  4   and they total   4
-- Cows =  5   Pigs =  7   Dogs =  0   and they total  12
-- Cows =  0   Pigs =  0   Dogs =  7   and they total   7
-- Cows =  2   Pigs =  3   Dogs =  4   and they total   9
-- Cows =  0   Pigs =  0   Dogs =  0   and they total   0

