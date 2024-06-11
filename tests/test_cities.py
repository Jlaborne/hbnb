import unittest
import uuid
from datetime import datetime
from model.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City('New York', uuid.uuid4())

    def test_city_creation(self):
        self.assertIsInstance(self.city.id, uuid.UUID)
        self.assertEqual(self.city.name, 'New York')
        self.assertIsInstance(self.city.country_id, uuid.UUID)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertEqual(self.city.created_at, self.city.updated_at)

if __name__ == '__main__':
    unittest.main()
