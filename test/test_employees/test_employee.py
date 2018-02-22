import unittest
from employees import Employee
from contracts import Voluntary, Fixed, Hourly
from cards import Card
from salary_calculators import VoluntaryCalculator, FixedCalculator, HourlyCalculator


class TestHourlyCalculator(unittest.TestCase):


    def test_employee_can_change_its_contract(self):
        volunteer = Employee(Voluntary(), VoluntaryCalculator(), [Card(10)])
        volunteer.change_contract(Fixed(1000), FixedCalculator())

        self.assertIsInstance(volunteer.contract(), Fixed, "Contract doesn't match")
        self.assertIsInstance(volunteer.calculator(), FixedCalculator, "Salary calculator doesn't match")
        self.assertFalse(volunteer.give_cards(), "Cards hasn't been reset")


    def test_employee_can_change_its_contract_and_preserve_pending_salary(self):
        employee = Employee(Hourly(10), HourlyCalculator(), [Card(10)])
        employee.change_contract(Fixed(500), FixedCalculator())

        self.assertIsInstance(employee.contract(), Fixed, "Contract doesn't match")
        self.assertIsInstance(employee.calculator(), FixedCalculator, "Salary calculator doesn't match")
        self.assertFalse(employee.give_cards(), "Cards hasn't been reset")
        self.assertEquals(employee.obtain_pending_salary(), 100, "Pending salary hasn't been recorded")
