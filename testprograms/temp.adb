with Ada.Text_IO;
use  Ada.Text_IO;

procedure h is 
type Degrees is new Float range -273.15 .. Float'Last;
Temperature : Degrees;
begin
	Temperature := Degrees(38);
if Temperature >= 40.0 then
    Put_Line ("Wow!");
    Put_Line ("It's extremely hot");
elsif Temperature >= 30.0 then
    Put_Line ("It's hot");
elsif Temperature >= 20.0 then
    Put_Line ("It's warm");
elsif Temperature >= 10.0 then
    Put_Line ("It's cool");
elsif Temperature >= 0.0 then
    Put_Line ("It's cold");
else
    Put_Line ("It's freezing");
end if;

case Temperature  is
   when 1 =>

      Walk_The_Dog;

   when 5 =>

      Launch_Nuke;

   when 8 | 10 =>

      Sell_All_Stock;

   when others =>

      Self_Destruct;

end case;

end h ;  

