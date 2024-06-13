import json
import os
import uuid
from datetime import datetime

DATA_DIR = 'data'  # Directory to store JSON files
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def get_file_path(entity_name):
    return os.path.join(DATA_DIR, f'{entity_name.lower()}.json')

def load_entities(entity_name):
    file_path = get_file_path(entity_name)
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_entities(entity_name, entities):
    file_path = get_file_path(entity_name)
    with open(file_path, 'w') as f:
        json.dump(entities, f, indent=4)

def create_entity(entity_name, entity_data):
    entities = load_entities(entity_name)
    entity_data['created_at'] = datetime.utcnow().isoformat()
    entity_data['updated_at'] = datetime.utcnow().isoformat()
    entities.append(entity_data)
    save_entities(entity_name, entities)

def update_entity(entity_name, entity_id, updated_data):
    entities = load_entities(entity_name)
    for entity in entities:
        if entity.get('id') == entity_id:
            entity.update(updated_data)
            entity['updated_at'] = datetime.utcnow().isoformat()
            save_entities(entity_name, entities)
            return True
    return False

def delete_entity(entity_name, entity_id):
    entities = load_entities(entity_name)
    filtered_entities = [entity for entity in entities if entity.get('id') != entity_id]
    save_entities(entity_name, filtered_entities)

def get_entity_by_id(entity_name, entity_id):
    entities = load_entities(entity_name)
    for entity in entities:
        if entity.get('id') == entity_id:
            return entity
    return None

def get_entities(entity_name):
    return load_entities(entity_name)
