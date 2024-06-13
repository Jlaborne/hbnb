import uuid
from datetime import datetime, timezone
import persistence.data_manager as data_manager

class Place:
    def __init__(self, name, description, address, city, latitude, longitude,
                 host_id, number_of_rooms, number_of_bathrooms, price_per_night,
                 max_guests, amenities=None, reviews=None):
        self.id = uuid.uuid4().hex  # Generate UUID4 for unique identifier
        self.created_at = datetime.now(timezone.utc).isoformat()  # Record creation timestamp
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities if amenities else []
        self.reviews = reviews if reviews else []

    def save(self):
        place_data = {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenities': self.amenities,
            'reviews': self.reviews
        }
        data_manager.create_entity('Place', place_data)

    @staticmethod
    def get_by_id(place_id):
        return data_manager.get_entity_by_id('Place', place_id)

    @staticmethod
    def update(place_id, updated_data):
        updated_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        return data_manager.update_entity('Place', place_id, updated_data)

    @staticmethod
    def delete(place_id):
        data_manager.delete_entity('Place', place_id)

    @staticmethod
    def get_all():
        return data_manager.get_entities('Place')
                     
    @staticmethod
    def is_valid_host(user_id):
        # Implement logic to check if the user is a host
        # This could involve checking if is_host=True for the user
        pass

    def create_place(self):
        if not self.is_valid_host(self.host_id):
            return False  # Host is not valid, place creation fails
        return True
