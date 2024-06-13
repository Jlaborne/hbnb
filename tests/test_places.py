import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from model.place import Place
from model.user import User
from model.amenity import Amenity

class TestPlace(unittest.TestCase):
    
    def setUp(self):
        # Setup initial data
        self.data_manager_patch = patch('place.DataManager')
        self.mock_data_manager = self.data_manager_patch.start()
        
        self.user = User("1", "Alice", "alice@example.com")
        self.owner = User("2", "Bob", "bob@example.com")
        self.place = Place("Charming Apartment", "A lovely place in the heart of the city", "123 Main St", "Paris", 48.8566, 2.3522, self.owner.id, 2, 1, 100, 4)
        
        self.mock_data_manager.add_review = MagicMock(return_value="review1")
        self.mock_data_manager.update = MagicMock(return_value=None)
        self.mock_data_manager.get_review = MagicMock(return_value={
            'id': 'review1',
            'user_id': self.user.id,
            'place_id': self.place.id,
            'content': "Great place!",
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        })

    def tearDown(self):
        self.data_manager_patch.stop()

    def test_add_review(self):
        self.place.add_review(self.user, "Great place, very clean and well located!")
        
        self.assertIn("review1", self.place.reviews)
        self.assertIn("review1", self.user.reviews)
        self.mock_data_manager.add_review.assert_called_once_with(self.user.id, self.place.id, "Great place, very clean and well located!")
        self.mock_data_manager.update.assert_any_call("users", self.user)
        self.mock_data_manager.update.assert_any_call("places", self.place)

    def test_add_review_by_owner(self):
        with self.assertRaises(ValueError):
            self.place.add_review(self.owner, "I love my own place!")

    def test_update_review(self):
        self.place.add_review(self.user, "Great place, very clean and well located!")
        self.place.update_review("review1", "Updated content")
        
        updated_review = self.mock_data_manager.get_review("review1")
        self.assertEqual(updated_review['content'], "Updated content")
        self.mock_data_manager.update.assert_any_call("reviews", updated_review)
        self.mock_data_manager.update.assert_any_call("places", self.place)

    def test_delete_review(self):
        self.place.add_review(self.user, "Great place, very clean and well located!")
        self.place.delete_review("review1")
        
        self.assertNotIn("review1", self.place.reviews)
        self.mock_data_manager.delete.assert_called_once_with("reviews", self.mock_data_manager.get_review("review1"))
        self.mock_data_manager.update.assert_called_with("places", self.place)

    def test_add_amenity(self):
        wifi = Amenity("1", "Wi-Fi")
        self.place.add_amenity(self.owner, wifi)
        
        self.assertIn(wifi, self.place.amenities)
        self.mock_data_manager.update.assert_called_with("places", self.place)

    def test_add_amenity_by_non_owner(self):
        wifi = Amenity("1", "Wi-Fi")
        with self.assertRaises(ValueError):
            self.place.add_amenity(self.user, wifi)

if __name__ == '__main__':
    unittest.main()
