class Employee(object):

    _cards = []

    def __init__(self, contract, salary_calculator, cards=[]):
        self._contract = contract
        self._salary_calculator = salary_calculator
        self._cards = cards
        self._pending_salary = 0

    def contract(self):
        return self._contract

    def change_contract(self, new_contract, new_calculator):
        self._pending_salary = self._salary_calculator.calculate(self)
        self._cards = []
        self._salary_calculator = new_calculator
        self._contract = new_contract

    def add_card(self, card):
        self._cards.append(card)

    def give_cards(self):
        return self._cards

    def obtain_salary(self):
        return self._salary_calculator.calculate(self)

    def obtain_pending_salary(self):
        return self._pending_salary
