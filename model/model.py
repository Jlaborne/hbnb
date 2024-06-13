import uuid
from datetime import datetime
import persistence.data_manger
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
        self.places_hosted = []  # List to store place_ids hosted by the user
        self.reviews_written = []  # List to store review_ids written by the user
    
    def host_place(self, place_id):
        self.places_hosted.append(place_id)

class Place:
    def __init__(self, name, description, address, city, latitude, longitude,
                 host_id, number_of_rooms, number_of_bathrooms, price_per_night,
                 max_guests, amenities=None, reviews=None):
        self.place_id = uuid.uuid4().hex
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
                     
    @staticmethod
    def is_valid_host(user_id):
        # Implement logic to check if the user is a host
        # This could involve checking if is_host=True for the user
        pass

    def create_place(self):
        if not self.is_valid_host(self.host_id):
            return False  # Host is not valid, place creation fails
        return True

class Review:
    def __init__(self, user_id, place_id, rating, comment):
        self.review_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def submit_review(self):
        pass

class Amenity:
    def __init__(self, name, description):
        self.amenity_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.name = name
        self.description = description
    @staticmethod
    def add_new_amenity(name, description):
        # Implement logic to add a new amenity to the catalog
        pass

class City:
    def __init__(self, name, country):
        self.city_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.name = name
        self.country = country

class Country:
    def __init__(self, name):
        self.country_id = uuid.uuid4().hex
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.name = name
        self.cities = []  # List to store city objects

    def add_city(self, city):
        self.cities.append(city)
