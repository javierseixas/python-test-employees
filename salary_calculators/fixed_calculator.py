class FixedCalculator(object):

    def calculate(self, employee):
        return employee.contract().salary()
