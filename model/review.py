import uuid
from datetime import datetime, timezone
import persistence.data_manager as data_manager

class Review:
    def __init__(self, user_id, place_id, content):
        self.id = uuid.uuid4().hex  # Generate a unique identifier for the review
        self.user_id = user_id
        self.place_id = place_id
        self.content = content
        self.created_at = datetime.now(timezone.utc).isoformat()  # Record creation timestamp
        self.updated_at = self.created_at

    def __str__(self):
        return f"Review by User {self.user_id} for Place {self.place_id}: {self.content}"

    def save(self):
        review_data = {
            'id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
        data_manager.create_entity('Review', review_data)

    @staticmethod
    def get_by_id(review_id):
        return data_manager.get_entity_by_id('Review', review_id)

    @staticmethod
    def update(review_id, updated_data):
        updated_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        return data_manager.update_entity('Review', review_id, updated_data)

    @staticmethod
    def delete(review_id):
        data_manager.delete_entity('Review', review_id)

    @staticmethod
    def get_all():
        return data_manager.get_entities('Review')

    @staticmethod
    def get_by_place_id(place_id):
        all_reviews = data_manager.get_entities('Review')
        return [review for review in all_reviews if review['place_id'] == place_id]

    @staticmethod
    def get_by_user_id(user_id):
        all_reviews = data_manager.get_entities('Review')
        return [review for review in all_reviews if review['user_id'] == user_id]
