import unittest
from unittest.mock import patch
from datetime import datetime, timezone
import uuid
from model.user import User
import persistence.data_manager as data_manager


class TestUser(unittest.TestCase):

    @patch('persistence.data_manager.create_entity')
    def test_save_user(self, mock_create_entity):
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        user.save()
        user_data = {
            'user_id': user.user_id,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
            'email': user.email,
            'password': user.password,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_host': user.is_host,
            'places_hosted': user.places_hosted,
            'reviews_written': user.reviews_written
        }
        mock_create_entity.assert_called_once_with('User', user_data)

    @patch('persistence.data_manager.get_entity_by_id')
    def test_get_by_id(self, mock_get_entity_by_id):
        user_id = str(uuid.uuid4().hex)
        user_data = {
            'user_id': user_id,
            'created_at': datetime.now(timezone.utc).isoformat(),
            'updated_at': datetime.now(timezone.utc).isoformat(),
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe',
            'is_host': False,
            'places_hosted': [],
            'reviews_written': []
        }
        mock_get_entity_by_id.return_value = user_data
        user = User.get_by_id(user_id)
        self.assertEqual(user['user_id'], user_id)
        self.assertEqual(user['email'], 'test@example.com')

    @patch('persistence.data_manager.update_entity')
    def test_update_user(self, mock_update_entity):
        user_id = str(uuid.uuid4().hex)
        updated_data = {'first_name': 'Jane'}
        User.update(user_id, updated_data)
        mock_update_entity.assert_called_once_with('User', user_id, updated_data)

    @patch('persistence.data_manager.delete_entity')
    def test_delete_user(self, mock_delete_entity):
        user_id = str(uuid.uuid4().hex)
        User.delete(user_id)
        mock_delete_entity.assert_called_once_with('User', user_id)

    @patch('persistence.data_manager.get_entities')
    def test_get_all_users(self, mock_get_entities):
        user_data = [
            {
                'user_id': str(uuid.uuid4().hex),
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat(),
                'email': 'test@example.com',
                'password': 'password',
                'first_name': 'John',
                'last_name': 'Doe',
                'is_host': False,
                'places_hosted': [],
                'reviews_written': []
            }
        ]
        mock_get_entities.return_value = user_data
        users = User.get_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['email'], 'test@example.com')

    def test_user_creation(self):
        email = 'test@example.com'
        password = 'password'
        first_name = 'John'
        last_name = 'Doe'
        user = User(email, password, first_name, last_name)
        
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertTrue(user.user_id)  # Check if user_id is set
    
    def test_unique_email_constraint(self):
        email = 'test@example.com'
        password = 'password'
        first_name = 'John'
        last_name = 'Doe'
        user1 = User(email, password, first_name, last_name)
        user1.save()  # Save the first user
        
        # Attempt to create another user with the same email
        with self.assertRaises(Exception):  # Adjust the type of exception based on your implementation
            user2 = User(email, 'anotherpassword', 'Jane', 'Smith')
            user2.save()

    def test_host_assignment(self):
        user = User('host@example.com', 'password', 'Host', 'User', is_host=True)
        place_id = str(uuid.uuid4().hex)
        user.host_place(place_id)
        
        self.assertIn(place_id, user.places_hosted)
    
    def tearDown(self):
        # Clean up after tests if necessary
        for user_data in User.get_all():
            User.delete(user_data['user_id'])

if __name__ == '__main__':
    unittest.main()

