import json
import os
from datetime import datetime, timezone

DATA_DIR = 'data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def create_entity(entity_type, entity_data):
    file_path = os.path.join(DATA_DIR, f'{entity_type}.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(entity_data)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_entity_by_id(entity_type, entity_id):
    file_path = os.path.join(DATA_DIR, f'{entity_type}.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            entity_key = get_entity_key(entity_type)
            for entity in data:
                if entity[entity_key] == entity_id:
                    return entity
    except FileNotFoundError:
        return None
    return None

def update_entity(entity_type, entity_id, updated_data):
    file_path = os.path.join(DATA_DIR, f'{entity_type}.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            entity_key = get_entity_key(entity_type)
            for entity in data:
                if entity[entity_key] == entity_id:
                    entity.update(updated_data)
                    entity['updated_at'] = datetime.now(timezone.utc).isoformat()
                    break
            else:
                return False

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except FileNotFoundError:
        return False

def delete_entity(entity_type, entity_id):
    file_path = os.path.join(DATA_DIR, f'{entity_type}.json')
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            entity_key = get_entity_key(entity_type)
            data = [entity for entity in data if entity.get(entity_key) != entity_id]

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        pass

def get_entities(entity_type):
    file_path = os.path.join(DATA_DIR, f'{entity_type}.json')
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def get_entity_key(entity_type):
    entity_keys = {
        'User': 'user_id',
        'Place': 'place_id',
        'Review': 'review_id',
        'Amenity': 'amenity_id',
        'City': 'city_id',
        'Country': 'country_id'
    }
    return entity_keys.get(entity_type)
