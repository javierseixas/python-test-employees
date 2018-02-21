from contracts.contract import Contract


class Fixed(Contract):

    def __init__(self, salary):
        self._salary = salary

    def salary(self):
        return self._salary
