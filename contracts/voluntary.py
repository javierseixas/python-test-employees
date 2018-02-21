from contracts.contract import Contract


class Voluntary(Contract):

    SALARY = 0

    def salary(self):
        return self.SALARY
