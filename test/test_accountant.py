import unittest
from mock import Mock
from accountant import Accountant

class TestAccountant(unittest.TestCase):

    def test_calculates_staff_total_salary(self):
        accountant = Accountant()
        staff = Mock()
        staff.obtain_salary = Mock(return_value=6000)
        result = accountant.calculate_staff_salary(staff)
        expected = 6000


