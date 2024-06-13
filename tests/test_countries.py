import unittest
from unittest.mock import patch, MagicMock
from model.country import Country, City
import persistence.data_manager as data_manager

class TestCountry(unittest.TestCase):

    def setUp(self):
        # Mock data for testing
        self.country_data = [
            {'country_id': '1', 'name': 'Country A', 'cities': [], 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'},
            {'country_id': '2', 'name': 'Country B', 'cities': [], 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'}
        ]
        self.city_data = [
            {'city_id': '1', 'name': 'City A', 'country': '1', 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'},
            {'city_id': '2', 'name': 'City B', 'country': '1', 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'},
            {'city_id': '3', 'name': 'City C', 'country': '2', 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'}
        ]
        data_manager.get_entities = MagicMock(side_effect=[self.country_data, self.city_data])

    @patch('persistence.data_manager.update_entity')
    def test_update_country(self, mock_update_entity):
        # Arrange
        country_id = '1'
        updated_data = {'name': 'Updated Country Name'}
        mock_update_entity.return_value = True
        
        # Act
        result = Country.update(country_id, updated_data)
        retrieved_country = Country.get_by_id(country_id)
        
        # Assert
        self.assertTrue(result)
        if retrieved_country:
            self.assertEqual(retrieved_country.name, 'Updated Country Name')
        else:
            self.fail(f"Country with ID '{country_id}' not found.")

    @patch('persistence.data_manager.create_entity')
    def test_create_country(self, mock_create_entity):
        # Arrange
        country_name = 'New Country'
        mock_create_entity.return_value = None
        
        # Act
        country = Country(country_name)
        country.save()
        retrieved_country = Country.get_by_id(country.country_id)
        
        # Assert
        if retrieved_country:
            self.assertEqual(retrieved_country.name, country_name)
        else:
            self.fail("Failed to create country.")

    def test_get_all_countries(self):
        # Act
        countries = Country.get_all()
        
        # Assert
        self.assertEqual(len(countries), 2)

class TestCity(unittest.TestCase):

    def setUp(self):
        # Mock data for testing
        self.country_data = [
            {'country_id': '1', 'name': 'Country A', 'cities': [], 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'},
            {'country_id': '2', 'name': 'Country B', 'cities': [], 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'}
        ]
        self.city_data = [
            {'city_id': '1', 'name': 'City A', 'country': '1', 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'},
            {'city_id': '2', 'name': 'City B', 'country': '1', 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'},
            {'city_id': '3', 'name': 'City C', 'country': '2', 'created_at': '2023-01-01T12:00:00Z', 'updated_at': '2023-01-01T12:00:00Z'}
        ]
        data_manager.get_entities = MagicMock(side_effect=[self.country_data, self.city_data])

    def test_get_all_cities(self):
        # Act
        cities = City.get_all()
        
        # Assert
        self.assertEqual(len(cities), 3)

if __name__ == '__main__':
    unittest.main()

