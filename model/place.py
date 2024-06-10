import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, address, city, latitude, longitude, host, num_rooms, bathrooms, price_per_night, max_guests, amenities=None, reviews=None):
        self.id = uuid.uuid4()  # Unique ID
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.num_rooms = num_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities if amenities is not None else []
        self.reviews = reviews if reviews is not None else []
        self.created_at = datetime.now()  # Creation Date
        self.updated_at = self.created_at  # Update Date
