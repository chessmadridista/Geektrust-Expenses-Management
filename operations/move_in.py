class MoveIn:
  
  
  def __init__(self):
    pass

  def __set_move_in(self, words_in_input_command, number_of_people, people):
    name = words_in_input_command[1]
    MAX_NUMBER_OF_PEOPLE = 3

    if number_of_people < MAX_NUMBER_OF_PEOPLE:
      number_of_people += 1
      people.append(name)
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message, number_of_people, people
