#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime, timedelta
from model.user import User  # Assuming the User class is in user.py

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('john.doe@example.com', 'securepassword123', 'John', 'Doe')

    def test_user_creation(self):
        self.assertIsInstance(self.user.id, uuid.UUID)
        self.assertEqual(self.user.email, 'john.doe@example.com')
        self.assertEqual(self.user.get_password(), 'securepassword123')
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_unique_email_constraint(self):
        # Test creating multiple users with the same email
        email = 'john.doe@example.com'
        user1 = User(email, 'securepassword123', 'John', 'Doe')
        with self.assertRaises(ValueError):
            user2 = User(email, 'anotherpassword123', 'Jane', 'Doe')

    def test_valid_user_creation(self):
        # Test valid user creation
        user = User('john.doe1@example.com', 'securepassword123', 'John', 'Doe')
        self.assertIsNotNone(user)
    
    def test_invalid_user_creation_missing_fields(self):
        # Test invalid user creation with missing fields
        with self.assertRaises(TypeError):
            user = User('john.doe2@example.com', 'securepassword123')

    def test_invalid_user_creation_invalid_email(self):
        # Test invalid user creation with invalid email format
        with self.assertRaises(ValueError):
            user = User('invalidemail', 'securepassword123', 'John', 'Doe')

    def test_add_review(self):
        initial_updated_at = self.user.updated_at
        self.user.add_review('Great place!')
        self.assertIn('Great place!', self.user.reviews)
        self.assertNotEqual(self.user.updated_at, initial_updated_at)

    def test_password_change(self):
        initial_updated_at = self.user.updated_at
        self.user.set_password('newpassword123')
        self.assertEqual(self.user.get_password(), 'newpassword123')
        self.assertNotEqual(self.user.updated_at, initial_updated_at)
if __name__ == '__main__':
    unittest.main()
