import unittest
import uuid
from datetime import datetime
from model.amenity import Amenity  # Assuming the Amenity class is in amenity.py

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity('Wi-Fi')

    def test_amenity_creation(self):
        self.assertIsInstance(self.amenity.id, uuid.UUID)
        self.assertEqual(self.amenity.name, 'Wi-Fi')
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertEqual(self.amenity.created_at, self.amenity.updated_at)

if __name__ == '__main__':
    unittest.main()
