case User_Choice is
         when 'A'    => Item := Terminal_IO.Get ("Item to add");
         when 'D'    => Item := Terminal_IO.Get ("Item to delete");
         when 'M'    => Item := Terminal_IO.Get ("Item to modify");
         when 'Q'    => exit Do_Menu_Choices_1;
  
         when others => -- error has already been signaled to user
            null;
      end case;

