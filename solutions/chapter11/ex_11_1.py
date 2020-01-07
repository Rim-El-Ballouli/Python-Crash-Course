import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        fun_result = city_country('santiago', 'chile')
        self.assertEqual(fun_result, 'Santiago, Chile')

if __name__ == '__main__': #in new versions of python 3.* unittest.main() must be under main
    unittest.main()