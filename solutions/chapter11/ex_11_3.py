import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Danny', 'Donald', 60000)
        self.currentSalary = self.employee.annual_salary

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, self.currentSalary + 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.annual_salary, self.currentSalary + 8000)

if __name__ == '__main__': #in new versions of python 3.* unittest.main() must be under main
    unittest.main()