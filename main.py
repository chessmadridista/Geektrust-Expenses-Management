class ExpensesCalculator:
  __number_of_people_in_empty_house = 0
  __min_number_of_people = 2
  __max_number_of_people = 3

  def __init__(self):
    self.__number_of_people = 0
    self.__people = list()
    self.__total_expenditure = dict()
    self.__amount_loaned = dict()
  
  def __set_move_in(self, words_in_input_command):
    name = words_in_input_command[1]

    if self.__number_of_people < self.__max_number_of_people:
      self.__number_of_people += 1
      self.__people.append(name)
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message
  
  
  
  def __get_member_existence(self, members):
    is_everyone_a_member = True
    
    for member in members:
      if member in self.__people:
        continue
      else:
        is_everyone_a_member = False
        break
    
    return is_everyone_a_member
  
  def __set_total_expenditure(self, spend_amount, members):
    member_owed = members[0]
    no_of_members = len(members)
    spend_amount //= no_of_members

    for member in members:
      if member in self.__total_expenditure:
        self.__total_expenditure[member] += spend_amount
      else:
        self.__total_expenditure[member] = spend_amount

    return True
  
  def __set_member_loans(self, spend_amount, member_owed, members):
    for member in members[1:]:
      if member in self.__amount_loaned[member_owed]:
        self.__amount_loaned[member_owed][member] += spend_amount
      else:
        self.__amount_loaned[member_owed][member] = spend_amount
    
    return True
  
  def __set_amount_loaned(self, spend_amount, members):
    member_owed = members[0]
    
    if member_owed in self.__amount_loaned:
      pass
    else:
      self.__amount_loaned[member_owed] = dict()
    
    self.__set_member_loans(spend_amount, member_owed, members)

    return True

  def __set_spend(self, words_in_input_command):
    spend_amount = int(words_in_input_command[1])
    members = words_in_input_command[2:]
    is_everyone_a_member = self.__get_member_existence(members)

    if is_everyone_a_member:
      self.__set_total_expenditure(spend_amount, members)
      self.__set_amount_loaned(spend_amount, members)
      message = "SUCCESS"
    else:
      message = "MEMBER_NOT_FOUND"

    return message

  def __get_dues(self, words_in_input_command):
    name = words_in_input_command[1]

    if self.__number_of_people > self.__number_of_people_in_empty_house:
      self.__number_of_people -= 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message

  def __set_clear_due(self, words_in_input_command):
    name = words_in_input_command[1]

    if self.__number_of_people > self.__number_of_people_in_empty_house:
      self.__number_of_people -= 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message
  
  def __has_dues(self, words_in_input_command):
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
  
  def __set_move_out(self, words_in_input_command):
    name = words_in_input_command[1]
    are_paid_dues_clear = self.__has_dues(words_in_input_command)
    are_received_dues_clear = self.__has_dues(words_in_input_command)

    if self.__number_of_people > self.__number_of_people_in_empty_house:
      self.__number_of_people -= 1
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message

  def __get_invalid_command(self):
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
      message = self.__set_move_in(words_in_input_command)
    elif command == command_spend:
      message = self.__set_spend(words_in_input_command)
    elif command == command_dues:
      message = self.__set_dues(words_in_input_command)
    elif command == command_clear_due:
      message = self.__set_clear_due(words_in_input_command)
    elif command == command_move_out:
      message = self.__set_move_out(words_in_input_command)
    else:
      message = self.__set_invalid_command()

    return message
  
  def main(self):
    input_command = self.__read_input_file()
    message = self.__set_command(input_command)

    return message

if __name__ == "__main__":
  calculator = ExpensesCalculator()

  print(calculator.main())