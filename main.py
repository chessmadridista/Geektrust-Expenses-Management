class ExpensesCalculator:
  __number_of_people_in_empty_house = 0
  __min_number_of_people = 2
  __max_number_of_people = 3

  def __init__(self):
    self.__number_of_people = 0
  
  def __move_in_new_person(self, name):
    if self.__number_of_people < self.__max_number_of_people:
      self.__number_of_people += 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message
  
  def __move_out_new_person(self, name):
    if self.__number_of_people > self.__number_of_people_in_empty_house:
      self.__number_of_people -= 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message
  
  def __check_command(self, input_command):
    words_in_input_command = input_command.split()
    command = words_in_input_command[0]
    command_move_in = "MOVE_IN"
    command_move_out = "MOVE_OUT"

    if command == command_move_in:
      name = words_in_input_command[1]
      message = self.__move_in_new_person(name)
    elif command == command_move_out:
      name = words_in_input_command[1]
      message = self.__move_out_new_person(name)

    return message
  
  def main(self, input_command):
    message = self.__check_command(input_command)

if __name__ == "__main__":
  calculator = ExpensesCalculator()