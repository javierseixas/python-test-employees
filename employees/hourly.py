from employees.employee import Employee


class Hourly(Employee):

    def __init__(self, salary_per_hour, cards=[]):
        self.cards = cards
        self.salary_per_hour = salary_per_hour

    def calculate_salary(self):
        return self._sum_cards_hours() * self.salary_per_hour

    def add_card(self, card):
        self.cards.append(card)

    def _sum_cards_hours(self):
        total = 0
        for card in self.cards:
            total += card.get_hours()
        return total
