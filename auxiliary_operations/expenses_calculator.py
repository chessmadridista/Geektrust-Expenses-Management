class ExpensesCalculator:
  __NUMBER_OF_PEOPLE_IN_EMPTY_HOUSE = 0
  __MIN_NUMBER_OF_PEOPLE = 2
  __MAX_NUMBER_OF_PEOPLE = 3

  def __init__(self):
    self.__number_of_people = 0
    self.__people = set() # E.g.: { "Sandy", "Mandy", "Pandy" }
    self.__total_expenditure = dict() # E.g.: { "Sandy": 90, "Mandy": 80, "Pandy": 70 }
    self.__amount_loaned = dict() # E.g.: { "Sandy": { "Mandy": 20, "Pandy": 0 }, "Mandy": { "Sandy": 20, "Pandy": 0 }, "Pandy": { "Mandy": 20, "Sandy": 0 } }