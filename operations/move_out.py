class MoveOut:
  @staticmethod
  def set_move_out(self, words_in_input_command):
    name = words_in_input_command[1]
    are_paid_dues_clear = self.__has_dues(words_in_input_command)
    are_received_dues_clear = self.__has_dues(words_in_input_command)

    if self.__number_of_people > self.__number_of_people_in_empty_house:
      self.__number_of_people -= 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message