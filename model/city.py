import uuid
from datetime import datetime
from persistence.storage import Storage

class City:
    storage = Storage()

    def __init__(self, name, country_code):
        self.id = str(uuid.uuid4())
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        City.storage.add_city(self)

    def update_city(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
        City.storage.update_city(self)

    def delete_city(self):
        City.storage.delete_city(self.id)
