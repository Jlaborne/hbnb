# Import necessary modules
import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, address, city, latitude, longitude,
                 host_id, number_of_rooms, number_of_bathrooms, price_per_night,
                 max_guests, amenities=None, reviews=None):
        self.place_id = uuid.uuid4().hex  # Generate UUID4 for unique identifier
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
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

class User:
    def __init__(self, email, password, first_name, last_name, is_host=False):
        self.user_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_host = is_host
        self.places_hosted = []
        self.reviews_written = []

class Review:
    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

class Amenity:
    def __init__(self, user_id, place_id, amenity):
        self.review_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.user_id = user_id
        self.place_id = place_id
        self.amenities = amenity

class City:
    def __init__(self, name, country):
        self.review_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.places = places if places else []

class Country:
    def __init__(self, name):
        self.name = name
      self.cities = cities if cities else []
# Define similar classes for Amenity, City, and any other entities
