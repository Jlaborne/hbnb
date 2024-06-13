import unittest
from model.user import User
from persistence.data_manager import DataManager

class TestUser(unittest.TestCase):

    def setUp(self):
        # Clear data before each test
        User.data_manager = DataManager()
        self.user = User(email='john@example.com', password='password123', first_name='John', last_name='Doe')
        self.user.save()

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'john@example.com')
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')

    def test_duplicate_email(self):
        with self.assertRaises(ValueError):
            User(email='john@example.com', password='newpassword', first_name='Jane', last_name='Doe')

    def test_password_management(self):
        self.assertEqual(self.user.get_password(), 'password123')
        initial_updated_at = self.user.updated_at
        self.user.set_password('newpassword')
        self.assertEqual(self.user.get_password(), 'newpassword')
        self.assertNotEqual(self.user.updated_at, initial_updated_at)

    def test_add_review(self):
        self.user.save()
        initial_updated_at = self.user.updated_at
        self.user.add_review('Great product!')
        user_from_db = User.get(self.user.id)
        self.assertIn('Great product!', user_from_db.reviews)
        self.assertNotEqual(self.user.updated_at, initial_updated_at)

    def test_find_by_email(self):
        self.user.save()
        found_user = User.find_by_email('john@example.com')
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.email, 'john@example.com')

    def test_str_representation(self):
        self.assertEqual(str(self.user), 'User: John Doe, Email: john@example.com')

if __name__ == '__main__':
    unittest.main()