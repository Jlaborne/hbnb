import uuid
from datetime import datetime
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data = {
            "users": {},
            "places": {},
            "reviews": {},
            "amenity": {},
            "country": {
                "US": {"code": "US", "name": "United States"},
                "CA": {"code": "CA", "name": "Canada"},
                "FR": {"code": "FR", "name": "France"},
                # Add more countries as needed
            },
            "city": {}
        }

    def save(self, entity_type, entity):
        if entity_type not in self.data:
            raise ValueError(f"Unknown entity type: {entity_type}")

        entity.id = str(uuid.uuid4())  # Generate unique ID
        entity.created_at = datetime.now()
        entity.updated_at = entity.created_at
        self.data[entity_type][entity.id] = entity  # Save entity to appropriate collection
        return entity

    def update(self, entity_type, entity):
        if entity_type not in self.data:
            raise ValueError(f"Unknown entity type: {entity_type}")

        entity.updated_at = datetime.now()
        self.data[entity_type][entity.id] = entity  # Update entity in appropriate collection
        return entity

    def delete(self, entity_type, entity_id):
        if entity_type not in self.data:
            raise ValueError(f"Unknown entity type: {entity_type}")

        if entity_id in self.data[entity_type]:
            del self.data[entity_type][entity_id]  # Delete entity from appropriate collection

    def get(self, entity_type, entity_id):
        if entity_type not in self.data:
            raise ValueError(f"Unknown entity type: {entity_type}")

        return self.data[entity_type].get(entity_id, None)  # Retrieve entity from appropriate collection

    def get_all(self, entity_type):
        if entity_type not in self.data:
            raise ValueError(f"Unknown entity type: {entity_type}")

        return list(self.data[entity_type].values())  # Get all entities of a specific type
