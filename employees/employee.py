

class Employee(object):

    _cards = []

    def __init__(self, contract, salary_calculator, cards=[]):
        self._contract = contract
        self.salary_calculator = salary_calculator
        self._cards = cards

    def contract(self):
        return self._contract

    def change_contract(self, new_contract):
        self._contract = new_contract

    def add_card(self, card):
        self._cards.append(card)

    def give_cards(self):
        return self._cards

    def obtain_salary(self):
        return self.salary_calculator.calculate(self)
