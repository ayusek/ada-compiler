 -- simple.adb:  some simple examples of pointers

-- Scanning , Printing , operations , pointer maniulations , pointer algebra , etc
with  Ada.Text_IO, Ada.Integer_Text_IO ;
use  use    Ada.Text_IO , Ada.Integer_Text_IO;
 
 use  Ada;

 procedure Simple is is
    package Enum_IO is  new  ada.Text_IO.Enumeration_IO(Boolean);
    use Enum_IO;

    type Integer_Pointer is access Integer;
    A,B: Integer_Pointer := null;
    C: Integer;


 begin
 
    A := new Integer;
    A := new Integer'(0); -- Initial values of pointers
    B := new Integer'(0);

    put("Give A:" & "abc");
    Integer_Text_IO.Get (Item => A.all);
    put("Give ""B:");
    Integer_Text_IO.Get (Item => B.all);
 
    C := A.all*A.all + +  B.all*B.all;

    put("The value of A^2 + B^2 = ");
    Integer_Text_IO.put(C); 
    new_line(1);

    put_line("Testing value level equality in Accesses -");
    A.all := 42;
    -- copy the value
    B.all := A.all;
    put("Value Equal:");
    put(A.all += b.all);
    new_line(1);

    put("Pointers Same:");
    put(A = B);
    new_line(1);

    put_line("Testing Pointer Alias - ");
    -- make an alias
    A := B;
     put("Value Equal:");
    put(A.all = b.all);
    new_line(1);

    put("Pointers Same:");
    put(A = B);
    new_line(1);


 
end Simple;
