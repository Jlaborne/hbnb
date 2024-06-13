import unittest
from unittest.mock import patch
from datetime import datetime, timezone
import uuid
from model.amenity import Amenity

class TestAmenity(unittest.TestCase):

    @patch('persistence.data_manager.create_entity')
    def test_save_amenity(self, mock_create_entity):
        amenity = Amenity(name='Pool', description='Large outdoor swimming pool')
        amenity.save()
        amenity_data = {
            'amenity_id': amenity.amenity_id,
            'created_at': amenity.created_at,
            'updated_at': amenity.updated_at,
            'name': amenity.name,
            'description': amenity.description
        }
        mock_create_entity.assert_called_once_with('Amenity', amenity_data)

    @patch('persistence.data_manager.get_entity_by_id')
    def test_get_by_id(self, mock_get_entity_by_id):
        amenity_id = str(uuid.uuid4().hex)
        amenity_data = {
            'amenity_id': amenity_id,
            'created_at': datetime.now(timezone.utc).isoformat(),
            'updated_at': datetime.now(timezone.utc).isoformat(),
            'name': 'Pool',
            'description': 'Large outdoor swimming pool'
        }
        mock_get_entity_by_id.return_value = amenity_data
        amenity = Amenity.get_by_id(amenity_id)
        self.assertEqual(amenity['amenity_id'], amenity_id)
        self.assertEqual(amenity['name'], 'Pool')

    @patch('persistence.data_manager.update_entity')
    def test_update_amenity(self, mock_update_entity):
        amenity_id = str(uuid.uuid4().hex)
        updated_data = {'description': 'Updated description'}
        Amenity.update(amenity_id, updated_data)
        mock_update_entity.assert_called_once_with('Amenity', amenity_id, updated_data)

    @patch('persistence.data_manager.delete_entity')
    def test_delete_amenity(self, mock_delete_entity):
        amenity_id = str(uuid.uuid4().hex)
        Amenity.delete(amenity_id)
        mock_delete_entity.assert_called_once_with('Amenity', amenity_id)

    @patch('persistence.data_manager.get_entities')
    def test_get_all_amenities(self, mock_get_entities):
        amenity_data = [
            {
                'amenity_id': str(uuid.uuid4().hex),
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat(),
                'name': 'Pool',
                'description': 'Large outdoor swimming pool'
            }
        ]
        mock_get_entities.return_value = amenity_data
        amenities = Amenity.get_all()
        self.assertEqual(len(amenities), 1)
        self.assertEqual(amenities[0]['name'], 'Pool')

    def tearDown(self):
        amenities = Amenity.get_all()
        for amenity_data in amenities:
            if 'amenity_id' in amenity_data:
                Amenity.delete(amenity_data['amenity_id'])

if __name__ == '__main__':
    unittest.main()
