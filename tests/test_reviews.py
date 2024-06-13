import unittest
from unittest.mock import patch
from datetime import datetime, timezone
import uuid
from model.review import Review

class TestReview(unittest.TestCase):

    @patch('persistence.data_manager.create_entity')
    def test_save_review(self, mock_create_entity):
        review = Review(user_id='user123', place_id='place123', content='Great place!')
        review.save()
        review_data = {
            'id': review.id,
            'user_id': review.user_id,
            'place_id': review.place_id,
            'content': review.content,
            'created_at': review.created_at,
            'updated_at': review.updated_at,
        }
        mock_create_entity.assert_called_once_with('Review', review_data)

    @patch('persistence.data_manager.get_entity_by_id')
    def test_get_by_id(self, mock_get_entity_by_id):
        review_id = str(uuid.uuid4().hex)
        review_data = {
            'id': review_id,
            'user_id': 'user123',
            'place_id': 'place123',
            'content': 'Great place!',
            'created_at': datetime.now(timezone.utc).isoformat(),
            'updated_at': datetime.now(timezone.utc).isoformat()
        }
        mock_get_entity_by_id.return_value = review_data
        review = Review.get_by_id(review_id)
        self.assertEqual(review['id'], review_id)
        self.assertEqual(review['content'], 'Great place!')

    @patch('persistence.data_manager.update_entity')
    def test_update_review(self, mock_update_entity):
        review_id = str(uuid.uuid4().hex)
        updated_data = {'content': 'Updated review content'}
        Review.update(review_id, updated_data)
        mock_update_entity.assert_called_once_with('Review', review_id, updated_data)

    @patch('persistence.data_manager.delete_entity')
    def test_delete_review(self, mock_delete_entity):
        review_id = str(uuid.uuid4().hex)
        Review.delete(review_id)
        mock_delete_entity.assert_called_once_with('Review', review_id)

    @patch('persistence.data_manager.get_entities')
    def test_get_all_reviews(self, mock_get_entities):
        review_data = [
            {
                'id': str(uuid.uuid4().hex),
                'user_id': 'user123',
                'place_id': 'place123',
                'content': 'Great place!',
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat()
            }
        ]
        mock_get_entities.return_value = review_data
        reviews = Review.get_all()
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['content'], 'Great place!')

    @patch('persistence.data_manager.get_entities')
    def test_get_by_place_id(self, mock_get_entities):
        review_data = [
            {
                'id': str(uuid.uuid4().hex),
                'user_id': 'user123',
                'place_id': 'place123',
                'content': 'Great place!',
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat()
            },
            {
                'id': str(uuid.uuid4().hex),
                'user_id': 'user124',
                'place_id': 'place123',
                'content': 'Another great review!',
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat()
            }
        ]
        mock_get_entities.return_value = review_data
        reviews = Review.get_by_place_id('place123')
        self.assertEqual(len(reviews), 2)
        self.assertEqual(reviews[0]['content'], 'Great place!')
        self.assertEqual(reviews[1]['content'], 'Another great review!')

    @patch('persistence.data_manager.get_entities')
    def test_get_by_user_id(self, mock_get_entities):
        review_data = [
            {
                'id': str(uuid.uuid4().hex),
                'user_id': 'user123',
                'place_id': 'place123',
                'content': 'Great place!',
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat()
            },
            {
                'id': str(uuid.uuid4().hex),
                'user_id': 'user123',
                'place_id': 'place124',
                'content': 'Not so great.',
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat()
            }
        ]
        mock_get_entities.return_value = review_data
        reviews = Review.get_by_user_id('user123')
        self.assertEqual(len(reviews), 2)
        self.assertEqual(reviews[0]['content'], 'Great place!')
        self.assertEqual(reviews[1]['content'], 'Not so great.')

    def tearDown(self):
        # Clean up after tests if necessary
        reviews = Review.get_all()
        for review_data in reviews:
            if 'id' in review_data:
                Review.delete(review_data['id'])

if __name__ == '__main__':
    unittest.main()
