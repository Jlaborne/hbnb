import uuid
from datetime import datetime
from persistence.data_manager import DataManager

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.amenities = []
        self.reviews = []  # List to store reviews

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
        self.updated_at = datetime.now()

    def add_review(self, user_id, content):
        review = {
            'id': str(uuid.uuid4()),
            'user_id': user_id,
            'content': content,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        self.reviews.append(review)
        self.updated_at = datetime.now()

    def update_review(self, review_id, new_content):
        for review in self.reviews:
            if review['id'] == review_id:
                review['content'] = new_content
                review['updated_at'] = datetime.now()
                self.updated_at = datetime.now()
                return

        raise ValueError(f"Review with ID {review_id} not found")

    def delete_review(self, review_id):
        for index, review in enumerate(self.reviews):
            if review['id'] == review_id:
                del self.reviews[index]
                self.updated_at = datetime.now()
                return

        raise ValueError(f"Review with ID {review_id} not found")

    def get_reviews(self):
        return self.reviews

    def __str__(self):
        return f"Place: {self.name}, Address: {self.address}, City ID: {self.city_id}, Host ID: {self.host_id}"
    