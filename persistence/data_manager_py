import uuid
from datetime import datetime
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data = {
            "users": {},
            "places": {},
            "reviews": {},
            "amenities": {},
            "countries": {
                "US": {"code": "US", "name": "United States"},
                "CA": {"code": "CA", "name": "Canada"},
                # Add more countries as needed
            },
            "cities": {}
        }

    def save(self, entity):
        entity_type = entity.__class__.__name__.lower()
        entity.id = str(uuid.uuid4())
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.data[entity_type][entity.id] = entity
        return entity

    def get(self, entity_id, entity_type):
        return self.data.get(entity_type, {}).get(entity_id, None)

    def update(self, entity):
        entity_type = entity.__class__.__name__.lower()
        entity.updated_at = datetime.now()
        self.data[entity_type][entity.id] = entity
        return entity

    def delete(self, entity_id, entity_type):
        if entity_id in self.data.get(entity_type, {}):
            del self.data[entity_type][entity_id]

    def get_all(self, entity_type):
        return list(self.data.get(entity_type, {}).values())
