def _has_dues(words_in_input_command):
  are_dues_clear = True
  dues = self.__get_dues(words_in_input_command)

  for due in dues:
    due_amount = due.split()

    if due_amount == "0":
      continue
    else:
      are_dues_clear = False
      break
  
  return are_dues_clear

def set_clear_due(words_in_input_command):
  name = words_in_input_command[1]

  if self.__number_of_people > self.__number_of_people_in_empty_house:
    self.__number_of_people -= 1
    message = "SUCCESS"
  else:
    message = "HOUSEFUL"
  
  return message