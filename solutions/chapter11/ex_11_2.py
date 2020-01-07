import unittest
from city_functions import city_country
from city_functions import city_country_population
from city_functions import city_country_population_optional

class TestCase(unittest.TestCase):
    # def test_city_country(self):
    #     fun_result = city_country('santiago', 'chile', 500)
    #     self.assertEqual(fun_result, 'Santiago, Chile')

    def test_city_country_population(self):
        fun_result = city_country_population('santiago', 'chile', 5000)
        self.assertEqual(fun_result, 'Santiago, Chile - 5000')

    def test_city_country_population_optional_1(self):
        fun_result = city_country_population_optional('santiago', 'chile', 5000)
        self.assertEqual(fun_result, 'Santiago, Chile - 5000')

    def test_city_country_population_optional_2(self):
        fun_result = city_country_population_optional('santiago', 'chile')
        self.assertEqual(fun_result, 'Santiago, Chile')

if __name__ == '__main__': #in new versions of python 3.* unittest.main() must be under main
    unittest.main()