from persistence.data_manager import DataManager
import uuid
from datetime import datetime

class City:
    data_manager = DataManager()

    def __init__(self, name, country):
        self.id = uuid.uuid4()  # Unique ID
        self.name = name
        self.country = country
        self.created_at = datetime.now()  # Creation Date
        self.updated_at = self.created_at  # Update Date

    def save(self):
        return City.data_manager.save(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return City.data_manager.update(self)

    def delete(self):
        return City.data_manager.delete(self.id, 'city')

    @classmethod
    def get(cls, city_id):
        return City.data_manager.get(city_id, 'city')

    @classmethod
    def get_all(cls):
        return City.data_manager.get_all('city')
