class MoveIn:
  def __init__(self):
    pass

  def __set_move_in(self, words_in_input_command):
    name = words_in_input_command[1]

    if self.__number_of_people < self.__max_number_of_people:
      self.__number_of_people += 1
      self.__people.append(name)
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message
