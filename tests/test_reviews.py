import unittest
import uuid
from datetime import datetime
from model.review import Review  # Assuming the Review class is in review.py

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review(uuid.uuid4(), uuid.uuid4(), 'Excellent stay!')

    def test_review_creation(self):
        self.assertIsInstance(self.review.id, uuid.UUID)
        self.assertIsInstance(self.review.user_id, uuid.UUID)
        self.assertIsInstance(self.review.place_id, uuid.UUID)
        self.assertEqual(self.review.content, 'Excellent stay!')
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertEqual(self.review.created_at, self.review.updated_at)

if __name__ == '__main__':
    unittest.main()
