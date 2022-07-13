import operations as op

class ExpensesCalculator:
  __NUMBER_OF_PEOPLE_IN_EMPTY_HOUSE = 0
  __MIN_NUMBER_OF_PEOPLE = 2
  __MAX_NUMBER_OF_PEOPLE = 3

  def __init__(self):
    self.__number_of_people = 0
    self.__people = list() # E.g.: ["Sandy", "Mandy", "Pandy"]
    self.__total_expenditure = dict() # E.g.: { "Sandy": 90, "Mandy": 80, "Pandy": 70 }
    self.__amount_loaned = dict() # E.g.: { "Sandy": { "Mandy": 20, "Pandy": 0 }, "Mandy": { "Sandy": 20, "Pandy": 0 }, "Pandy": { "Mandy": 20, "Sandy": 0 } }

  def __get_invalid_command_message(self):
    ERROR_MESSAGE = "The command is not valid! Please try again with a different command."

    return ERROR_MESSAGE
  
  def __get_input_file(self):
    pass

  def __set_command(self, input_command):
    words_in_input_command = input_command.split()
    command = words_in_input_command[0]
    COMMAND_MOVE_IN = "MOVE_IN"
    COMMAND_SPEND = "SPEND"
    COMMAND_DUES = "DUES"
    COMMAND_CLEAR_DUE = "CLEAR_DUE"
    COMMAND_MOVE_OUT = "MOVE_OUT"

    if command == COMMAND_MOVE_IN:
      message, self.__number_of_people, self.__people = op.move_in.MoveIn().__set_move_in(words_in_input_command, self.__number_of_people, self.__people)
    elif command == COMMAND_SPEND:
      message = op.spend.Spend().__set_spend(words_in_input_command)
    elif command == COMMAND_DUES:
      message = op.dues.Dues().__set_dues(words_in_input_command)
    elif command == COMMAND_CLEAR_DUE:
      message = op.clear_due.ClearDue().__set_clear_due(words_in_input_command)
    elif command == COMMAND_MOVE_OUT:
      message = op.move_out.MoveOut().__set_move_out(words_in_input_command)
    else:
      message = self.__get_invalid_command_message()

    return message
  
  def main(self):
    input_commands = self.__get_input_file()

    for command in input_commands:
      message = self.__set_command(command)

      yield message

if __name__ == "__main__":
  calculator = ExpensesCalculator()

  print(calculator.main())