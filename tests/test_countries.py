import unittest
import uuid
from model.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country('USA')

    def test_country_creation(self):
        self.assertIsInstance(self.country.id, uuid.UUID)
        self.assertEqual(self.country.name, 'USA')

if __name__ == '__main__':
    unittest.main()
