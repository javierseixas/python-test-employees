import unittest
from employees.employee import Employee
from contracts import Voluntary
from salary_calculators import VoluntaryCalculator


class TestFixedCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = VoluntaryCalculator()
        self.contract = Voluntary()
        self.employee = Employee(self.contract, self.calculator, [])


    def test_calculates_its_salary_correctly(self):
        result = self.calculator.calculate(self.employee)
        expected = Voluntary.SALARY

        self.assertEqual(expected, result)
