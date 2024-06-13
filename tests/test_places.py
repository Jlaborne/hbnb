import unittest
from datetime import datetime
from model.place import Place
from persistence.data_manager import DataManager

class TestPlace(unittest.TestCase):

    def setUp(self):
        # Set up a mock DataManager for testing
        self.data_manager = DataManager()
        self.place = Place(
            name="Cozy Apartment",
            description="A comfortable place to stay",
            address="123 Main St",
            city_id="NYC",
            latitude=40.7128,
            longitude=-74.0060,
            host_id="host123",
            num_rooms=2,
            num_bathrooms=1,
            price_per_night=100,
            max_guests=4
        )
        # Save the place to the mock DataManager
        self.place.save()

    def tearDown(self):
        # Clean up by deleting the place after each test
        self.place.delete()

    def test_add_review(self):
        initial_updated_at = self.place.updated_at
        review_content = "Great place to stay!"
        self.place.add_review(Review(user_id="user456", place_id=self.place.id, content=review_content))
        
        # Retrieve the place from the DataManager to get the updated version
        place_from_db = Place.get(self.place.id)
        
        # Check if the review is added and updated_at is changed
        self.assertEqual(len(place_from_db.get_reviews()), 1)
        self.assertIn(review_content, [review.content for review in place_from_db.get_reviews()])
        self.assertNotEqual(place_from_db.updated_at, initial_updated_at)

    def test_update_review(self):
        review_content = "Nice location"
        self.place.add_review(Review(user_id="user789", place_id=self.place.id, content=review_content))
        
        # Retrieve the place from the DataManager to get the updated version
        place_from_db = Place.get(self.place.id)

        updated_review_content = "Excellent location and cozy place!"
        review_to_update = place_from_db.get_reviews()[0]
        initial_updated_at = place_from_db.updated_at

        # Update the review
        self.place.update_review(review_to_update.id, updated_review_content)

        # Retrieve the place again to get the updated version
        place_from_db_after_update = Place.get(self.place.id)
        
        # Check if the review content and updated_at are updated correctly
        updated_review = next(review for review in place_from_db_after_update.get_reviews() if review.id == review_to_update.id)
        self.assertEqual(updated_review.content, updated_review_content)
        self.assertNotEqual(updated_review.updated_at, initial_updated_at)

    def test_delete_review(self):
        review_content = "Excellent service!"
        self.place.add_review(Review(user_id="user123", place_id=self.place.id, content=review_content))
        
        # Retrieve the place from the DataManager to get the updated version
        place_from_db = Place.get(self.place.id)
        
        initial_updated_at = place_from_db.updated_at

        # Delete the review
        review_to_delete = place_from_db.get_reviews()[0]
        self.place.delete_review(review_to_delete.id)

        # Retrieve the place again to get the updated version
        place_from_db_after_delete = Place.get(self.place.id)
        
        # Check if the review is deleted and updated_at is changed
        self.assertEqual(len(place_from_db_after_delete.get_reviews()), 0)
        self.assertNotEqual(place_from_db_after_delete.updated_at, initial_updated_at)

    def test_get_reviews(self):
        self.place.add_review(Review(user_id="user456", place_id=self.place.id, content="Nice view"))
        self.place.add_review(Review(user_id="user789", place_id=self.place.id, content="Great location"))

        # Retrieve reviews
        reviews = self.place.get_reviews()

        # Check if the correct number of reviews are retrieved
        self.assertEqual(len(reviews), 2)

        # Check if all added reviews are retrieved correctly
        self.assertIn("Nice view", [review.content for review in reviews])
        self.assertIn("Great location", [review.content for review in reviews])

if __name__ == '__main__':
    unittest.main()