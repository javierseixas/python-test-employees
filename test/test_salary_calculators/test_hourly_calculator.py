import unittest
from employees.employee import Employee
from contracts.hourly import Hourly
from salary_calculators.hourly_calculator import HourlyCalculator
from cards.card import Card


class TestHourlyCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = HourlyCalculator()
        self.contract = Hourly(10)
        self.employee = Employee(self.contract, self.calculator, [])


    def test_with_employee_with_one_card(self):
        self.employee.add_card(Card(10))

        result = self.calculator.calculate(self.employee)
        expected = 100

        self.assertEqual(expected, result)

    def test_with_employee_with_thre_cards(self):
        self.employee.add_card(Card(10))
        self.employee.add_card(Card(20))
        self.employee.add_card(Card(5))

        result = self.calculator.calculate(self.employee)
        expected = 350

        self.assertEqual(expected, result)

    def test_with_employee_with_no_cards(self):

        result = self.calculator.calculate(self.employee)
        expected = 0

        self.assertEqual(expected, result)
