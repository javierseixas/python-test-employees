import unittest
from employees import Employee
from contracts import Fixed
from salary_calculators import FixedCalculator


class TestFixedCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = FixedCalculator()
        self.contract = Fixed(10)
        self.employee = Employee(self.contract, self.calculator, [])


    def test_calculates_its_salary_correctly(self):
        result = self.calculator.calculate(self.employee)
        expected = 10

        self.assertEqual(expected, result)
