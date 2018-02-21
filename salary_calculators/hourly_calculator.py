class HourlyCalculator(object):

    def calculate_salary(self, employee):
        return self._sum_total_hours(employee.give_cards()) * employee.contract().salary()

    def _sum_total_hours(self, cards):
        total_hours = 0
        for card in cards:
            total_hours += card.get_hours()
        return total_hours
