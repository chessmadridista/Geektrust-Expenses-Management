import operations as op

class ExpensesCalculator:
  __number_of_people_in_empty_house = 0
  __min_number_of_people = 2
  __max_number_of_people = 3

  def __init__(self):
    self.__number_of_people = 0
    self.__people = list() # E.g.: ["Sandy", "Mandy", "Pandy"]
    self.__total_expenditure = dict() # E.g.: { "Sandy": 90, "Mandy": 80, "Pandy": 70 }
    self.__amount_loaned = dict() # E.g.: { "Sandy": { "Mandy": 20, "Pandy": 0 }, "Mandy": { "Sandy": 20, "Pandy": 0 }, "Pandy": { "Mandy": 20, "Sandy": 0 } }

  def __get_invalid_command_message(self):
    error_message = "The command is not valid! Please try again with a different command."

    return error_message
  
  def __read_input_file(self):
    pass

  def __set_command(self, input_command):
    words_in_input_command = input_command.split()
    command = words_in_input_command[0]
    command_move_in = "MOVE_IN"
    command_spend = "SPEND"
    command_dues = "DUES"
    command_clear_due = "CLEAR_DUE"
    command_move_out = "MOVE_OUT"

    if command == command_move_in:
      message = op.move_in.MoveIn().__set_move_in(words_in_input_command)
    elif command == command_spend:
      message = op.move_in.MoveIn().__set_spend(words_in_input_command)
    elif command == command_dues:
      message = op.move_in.MoveIn().__set_dues(words_in_input_command)
    elif command == command_clear_due:
      message = op.move_in.MoveIn().__set_clear_due(words_in_input_command)
    elif command == command_move_out:
      message = op.move_in.MoveIn().__set_move_out(words_in_input_command)
    else:
      message = self.__get_invalid_command_message()

    return message
  
  def main(self):
    input_commands = self.__read_input_file()
    message = self.__set_command(input_commands)

    return message

if __name__ == "__main__":
  calculator = ExpensesCalculator()

  print(calculator.main())