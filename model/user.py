import uuid
from datetime import datetime, timezone
import persistence.data_manager as data_manager
class User:
    def __init__(self, email, password, first_name, last_name, is_host=False):
        self.user_id = uuid.uuid4().hex  # Generate a unique ID for the user
        self.created_at = datetime.now(timezone.utc).isoformat()  # Record creation timestamp
        self.updated_at = datetime.now(timezone.utc).isoformat()  # Record last updated timestamp
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_host = is_host
        self.places_hosted = []  # List to store place_ids hosted by the user
        self.reviews_written = []  # List to store review_ids written by the user
    
    def host_place(self, place_id):
        self.places_hosted.append(place_id)

    def save(self):
        # Check if the user with this email already exists
        existing_user = self.get_by_email(self.email)
        if existing_user:
            raise ValueError(f"User with email '{self.email}' already exists.")

        user_data = {
            'user_id': self.user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_host': self.is_host,
            'places_hosted': self.places_hosted,
            'reviews_written': self.reviews_written
        }
        data_manager.create_entity('User', user_data)

    @staticmethod
    def get_by_id(user_id):
        return data_manager.get_entity_by_id('User', user_id)
    
    @staticmethod
    def get_by_email(email):
        # Retrieve a user by their email
        users = data_manager.get_entities('User')
        for user in users:
            if user['email'] == email:
                return user
        return None
    
    @staticmethod
    def update(user_id, updated_data):
        updated_data['updated_at'] = datetime(timezone.utc).isoformat()
        return data_manager.update_entity('User', user_id, updated_data)

    @staticmethod
    def delete(user_id):
        data_manager.delete_entity('User', user_id)

    @staticmethod
    def get_all():
        return data_manager.get_entities('User')