import unittest
import uuid
from model.country import Country

class TestCountry(unittest.TestCase):

    def test_country_creation(self):
        country_namme = "USA"
        country = Country(country_namme)
        self.assertEqual(country.name, country_namme)

if __name__ == '__main__':
    unittest.main()
