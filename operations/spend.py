def _get_member_existence(self, members):
  is_everyone_a_member = True
  
  for member in members:
    if member in self.__people:
      continue
    else:
      is_everyone_a_member = False
      break
  
  return is_everyone_a_member

def _set_total_expenditure(self, spend_amount, members):
  member_owed = members[0]
  no_of_members = len(members)
  spend_amount //= no_of_members

  for member in members:
    if member in self.__total_expenditure:
      self.__total_expenditure[member] += spend_amount
    else:
      self.__total_expenditure[member] = spend_amount

  return True

def _set_member_loans(self, spend_amount, member_owed, members):
  for member in members[1:]:
    if member in self.__amount_loaned[member_owed]:
      self.__amount_loaned[member_owed][member] += spend_amount
    else:
      self.__amount_loaned[member_owed][member] = spend_amount
  
  return True

def _set_amount_loaned(cls, spend_amount, members):
  member_owed = members[0]
  
  if member_owed in cls.__amount_loaned:
    pass
  else:
    cls.__amount_loaned[member_owed] = dict()
  
  cls.__set_member_loans(spend_amount, member_owed, members)

  return True

def set_spend(cls, words_in_input_command):
  spend_amount = int(words_in_input_command[1])
  members = words_in_input_command[2:]
  is_everyone_a_member = cls.__get_member_existence(members)

  if is_everyone_a_member:
    cls.__set_total_expenditure(spend_amount, members)
    cls.__set_amount_loaned(spend_amount, members)
    message = "SUCCESS"
  else:
    message = "MEMBER_NOT_FOUND"

  return message