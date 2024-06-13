import uuid
from datetime import datetime, timezone
import persistence.data_manager as data_manager

class Amenity:
    def __init__(self, name, description):
        self.amenity_id = uuid.uuid4().hex
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.name = name
        self.description = description

    def save(self):
        amenity_data = {
            'amenity_id': self.amenity_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'description': self.description
        }
        data_manager.create_entity('Amenity', amenity_data)

    @staticmethod
    def get_by_id(amenity_id):
        return data_manager.get_entity_by_id('Amenity', amenity_id)

    @staticmethod
    def update(amenity_id, updated_data):
        updated_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        return data_manager.update_entity('Amenity', amenity_id, updated_data)

    @staticmethod
    def delete(amenity_id):
        data_manager.delete_entity('Amenity', amenity_id)

    @staticmethod
    def get_all():
        return data_manager.get_entities('Amenity')

    @staticmethod
    def add_new_amenity(name, description):
        amenity = Amenity(name, description)
        amenity.save()
        return amenity

# Example Usage
new_amenity = Amenity.add_new_amenity("Pool", "Large outdoor swimming pool")
print(new_amenity.amenity_id)
