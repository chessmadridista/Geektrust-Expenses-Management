def get_dues(self, words_in_input_command):
  name = words_in_input_command[1]

  if self.__number_of_people > self.__number_of_people_in_empty_house:
    self.__number_of_people -= 1
    message = "SUCCESS"
  else:
    message = "HOUSEFUL"
  
  return message