import unittest
import uuid
from datetime import datetime
from place import Place  # Assuming the Place class is in place.py

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place('Nice Apartment', 'A lovely place', '123 Main St', uuid.uuid4(), 40.7128, -74.0060, uuid.uuid4(), 2, 1, 100.0, 4)

    def test_place_creation(self):
        self.assertIsInstance(self.place.id, uuid.UUID)
        self.assertEqual(self.place.name, 'Nice Apartment')
        self.assertEqual(self.place.description, 'A lovely place')
        self.assertEqual(self.place.address, '123 Main St')
        self.assertIsInstance(self.place.city_id, uuid.UUID)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertIsInstance(self.place.host_id, uuid.UUID)
        self.assertEqual(self.place.num_rooms, 2)
        self.assertEqual(self.place.num_bathrooms, 1)
        self.assertEqual(self.place.price_per_night, 100.0)
        self.assertEqual(self.place.max_guests, 4)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertEqual(self.place.created_at, self.place.updated_at)

    def test_add_amenity(self):
        initial_updated_at = self.place.updated_at
        self.place.add_amenity('Wi-Fi')
        self.assertIn('Wi-Fi', self.place.amenities)
        self.assertNotEqual(self.place.updated_at, initial_updated_at)

if __name__ == '__main__':
    unittest.main()
