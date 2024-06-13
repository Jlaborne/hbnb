import unittest
from unittest.mock import patch
from datetime import datetime, timezone
import uuid
from model.place import Place
import persistence.data_manager as data_manager

class TestPlace(unittest.TestCase):

    @patch('persistence.data_manager.create_entity')
    def test_save_place(self, mock_create_entity):
        place = Place(
            name='Beautiful Cottage',
            description='A cozy cottage in the countryside.',
            address='123 Country Road',
            city='Countryside',
            latitude=45.0,
            longitude=-73.0,
            host_id='host123',
            number_of_rooms=2,
            number_of_bathrooms=1,
            price_per_night=100,
            max_guests=4
        )
        place.save()
        place_data = {
            'id': place.id,
            'created_at': place.created_at,
            'updated_at': place.updated_at,
            'name': place.name,
            'description': place.description,
            'address': place.address,
            'city': place.city,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'host_id': place.host_id,
            'number_of_rooms': place.number_of_rooms,
            'number_of_bathrooms': place.number_of_bathrooms,
            'price_per_night': place.price_per_night,
            'max_guests': place.max_guests,
            'amenities': place.amenities,
            'reviews': place.reviews
        }
        mock_create_entity.assert_called_once_with('Place', place_data)

    @patch('persistence.data_manager.get_entity_by_id')
    def test_get_by_id(self, mock_get_entity_by_id):
        place_id = str(uuid.uuid4().hex)
        place_data = {
            'id': place_id,
            'created_at': datetime.now(timezone.utc).isoformat(),
            'updated_at': datetime.now(timezone.utc).isoformat(),
            'name': 'Beautiful Cottage',
            'description': 'A cozy cottage in the countryside.',
            'address': '123 Country Road',
            'city': 'Countryside',
            'latitude': 45.0,
            'longitude': -73.0,
            'host_id': 'host123',
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 4,
            'amenities': [],
            'reviews': []
        }
        mock_get_entity_by_id.return_value = place_data
        place = Place.get_by_id(place_id)
        self.assertEqual(place['id'], place_id)
        self.assertEqual(place['name'], 'Beautiful Cottage')

    @patch('persistence.data_manager.update_entity')
    def test_update_place(self, mock_update_entity):
        place_id = str(uuid.uuid4().hex)
        updated_data = {'name': 'Updated Cottage'}
        Place.update(place_id, updated_data)
        mock_update_entity.assert_called_once_with('Place', place_id, updated_data)

    @patch('persistence.data_manager.delete_entity')
    def test_delete_place(self, mock_delete_entity):
        place_id = str(uuid.uuid4().hex)
        Place.delete(place_id)
        mock_delete_entity.assert_called_once_with('Place', place_id)

    @patch('persistence.data_manager.get_entities')
    def test_get_all_places(self, mock_get_entities):
        place_data = [
            {
                'id': str(uuid.uuid4().hex),
                'created_at': datetime.now(timezone.utc).isoformat(),
                'updated_at': datetime.now(timezone.utc).isoformat(),
                'name': 'Beautiful Cottage',
                'description': 'A cozy cottage in the countryside.',
                'address': '123 Country Road',
                'city': 'Countryside',
                'latitude': 45.0,
                'longitude': -73.0,
                'host_id': 'host123',
                'number_of_rooms': 2,
                'number_of_bathrooms': 1,
                'price_per_night': 100,
                'max_guests': 4,
                'amenities': [],
                'reviews': []
            }
        ]
        mock_get_entities.return_value = place_data
        places = Place.get_all()
        self.assertEqual(len(places), 1)
        self.assertEqual(places[0]['name'], 'Beautiful Cottage')
        
    @patch('persistence.data_manager.get_entity_by_id')
    def test_create_place_invalid_host(self, mock_get_entity_by_id):
        # Assuming is_valid_host returns False when the host is invalid
        mock_get_entity_by_id.return_value = {'is_host': False}
        place = Place(
            name='Beautiful Cottage',
            description='A cozy cottage in the countryside.',
            address='123 Country Road',
            city='Countryside',
            latitude=45.0,
            longitude=-73.0,
            host_id='host123',  # This should be invalid
            number_of_rooms=2,
            number_of_bathrooms=1,
            price_per_night=100,
            max_guests=4
        )
        self.assertFalse(place.create_place())  # Expecting False since host is invalid

    def tearDown(self):
        # Clean up after tests if necessary
        for place_data in Place.get_all():
            Place.delete(place_data['place_id'])

if __name__ == '__main__':
    unittest.main()