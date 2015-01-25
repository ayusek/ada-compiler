-- here function names are string. What should we do in that case.

-- unbounded.adb:  illustrating access to String
 
 procedure Unbounded is
 
    type Unbounded_String_Type is access String;
 
    function "<" (Left, Right: Unbounded_String_Type)
                  return Boolean is
    begin
       return (Left.all < Right.all);
    end "<";
 
    function "&" (Left, Right: Unbounded_String_Type)
                  return Unbounded_String_Type is
    begin
       return (new String'(Left.all & Right.all));
    end "&";
 
    W, X, Y, Z : Unbounded_String_Type;
 
 begin
 
    W := new String (1..0);   -- empty string
    W := new String (1..20);  -- allocate 20 characters
    X := new String'("Hello");
    Y := new String'(1..10=>'J');
    Z := new String'(X.all & ' ' & "Mildred"); -- "Hello Mildred"
 
    W := X;                   -- now W points to 5 characters
 
    W := new String'(X.all);  -- allocate new string and copy
 
 end Unbounded;

