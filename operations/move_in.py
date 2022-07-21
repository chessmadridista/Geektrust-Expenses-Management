class MoveIn:
  __MAX_NUMBER_OF_PEOPLE = 3

  def __init__(self):
    pass

  @classmethod
  def __set_move_in(cls, words_in_input_command, number_of_people, people):
    name = words_in_input_command[1]

    if number_of_people < cls.__MAX_NUMBER_OF_PEOPLE:
      number_of_people += 1
      people.add(name)
      message = "SUCCESS"
    else:
      message = "HOUSEFUL"
    
    return message, number_of_people, people
