-- compare.adb:  comparing arrays and array slices

with Ada.Text_IO , Ada.Integer_Text_Io , Ada.Float_Text_Io;
use Ada,  Ada.Text_IO , Ada.Integer_Text_Io;

procedure Compare is
begin
declare
-- <> are used to give unknown sub-range
type Integer_Array is array (Positive range <>) of Integer;
Max_Entries : constant Integer := 400;
S: Integer_Array := (31, 32, 33, 34, 35);
L: Integer_Array := (21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 41);
begin
put("Prinitng a Constant");
put(Max_entries);
put("The First Element of S is:");
put(S(1));
new_line(1);
Put_Line (Boolean'Image (  S       = L         ));   -- false
Put_Line (Boolean'Image (  S       < L         ));   -- false
Put_Line (Boolean'Image (  S       = L(1..5)   ));   -- false
Put_Line (Boolean'Image (  S       = L(6..10)  ));   -- true
Put_Line (Boolean'Image (  S(1..4) < L(6..10)  ));   -- true
end;

--Another Block
declare
type Month is (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec);
type Month_Array is array (Positive range <>) of Month;
S: Month_Array := (Jun,Jul,Aug,Sep,Oct);
L: Month_Array := (Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Dec);
begin
Put_Line (Boolean'Image (  S       = L         ));   -- false
Put_Line (Boolean'Image (  S       < L         ));   -- false
Put_Line (Boolean'Image (  S       = L(1..5)   ));   -- false
Put_Line (Boolean'Image (  S       = L(6..10)  ));   -- true
Put_Line (Boolean'Image (  S(1..4) < L(6..10)  ));   -- true
Put_Line (Boolean'Image (  S(5..1) < L         ));   -- true
end;

--Two Dimensional Arrays
--And Arrays of Arrays
declare 
subtype S1 is Integer range 1..5;
subtype S2 is Character range 'A'..'Z';
type Array_2D is array (S1,S2) of Float;
type Array_1D is array (S2) of Float;
type Array_Of_Array is array (S1) of Array_1D;

A: Array_1D;
B:Array_2D;
C:Array_Of_Array;

begin
    A := (S2 => 3.964129E15);
    B := (S1 => (S2 => 3.964129E15));
    C := (S1 => (S2 => 3.964129E15));
 
    -- Array indexing
    Float_Text_IO.Put (A ('Z'));
    Text_IO.New_Line;
    Float_Text_IO.Put (B (3, 'Z'));
    Text_IO.New_Line;
    Float_Text_IO.Put (C (3)('Z'));
    Text_IO.New_Line;

    A and  B or C xor d

end;

end Compare;


