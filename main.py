class ExpensesCalculator:
  __number_of_people_in_empty_house = 0
  __min_number_of_people = 2
  __max_number_of_people = 3

  def __init__(self):
    self.__number_of_people = 0
  
  def __process_move_in(self, words_in_input_command):
    name = words_in_input_command[1]

    if self.__number_of_people < self.__max_number_of_people:
      self.__number_of_people += 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message
  
  def __process_move_out(self, words_in_input_command):
    name = words_in_input_command[1]

    if self.__number_of_people > self.__number_of_people_in_empty_house:
      self.__number_of_people -= 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message

  def __process_invalid_command(self):
    error_message = "The command is not valid! Please try again with a different command."

    return error_message
  
  def __process_command(self, input_command):
    words_in_input_command = input_command.split()
    command = words_in_input_command[0]
    command_move_in = "MOVE_IN"
    command_move_out = "MOVE_OUT"
    command_spend = "SPEND"
    command_dues = "DUES"
    command_clear_due = "CLEAR_DUE"

    if command == command_move_in:
      message = self.__process_move_in(words_in_input_command)
    elif command == command_move_out:
      message = self.__process_move_out(words_in_input_command)
    elif command == command_spend:
      message = self.__process_move_out()
    elif command == command_dues:
      message = self.__process_move_out()
    elif command == command_clear_due:
      message = self.__process_move_out()
    else:
      message = self.__process_invalid_command()

    return message
  
  def main(self, input_command):
    message = self.__process_command(input_command)

    return message

if __name__ == "__main__":
  calculator = ExpensesCalculator()