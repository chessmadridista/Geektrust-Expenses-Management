class MoveIn:
  @staticmethod
  def set_move_in(words_in_input_command, number_of_people, people):
    name = words_in_input_command[1]
    MAX_NUMBER_OF_PEOPLE = 3

    if number_of_people < MAX_NUMBER_OF_PEOPLE:
      number_of_people += 1
      people.add(name)
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message, number_of_people, people
