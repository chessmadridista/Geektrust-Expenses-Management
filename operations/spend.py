class Spend:
  def __init__(self):
    pass

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