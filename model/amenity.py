import uuid
from datetime import datetime

class Amenity:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"Amenity: {self.name}"
