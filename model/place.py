import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
        self.id = uuid.uuid4()
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

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Place: {self.name}, Address: {self.address}, City ID: {self.city_id}, Host ID: {self.host_id}"
