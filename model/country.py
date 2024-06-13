import uuid
from datetime import datetime, timezone
import persistence.data_manager as data_manager

class City:
    def __init__(self, name, country):
        self.city_id = uuid.uuid4().hex
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.name = name
        self.country = country

    def save(self):
        city_data = {
            'city_id': self.city_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'country': self.country
        }
        data_manager.create_entity('City', city_data)

    @staticmethod
    def get_by_id(city_id):
        city_data = data_manager.get_entity_by_id('City', city_id)
        if city_data:
            return City(city_data['name'], city_data['country'])
        return None

    @staticmethod
    def update(city_id, updated_data):
        updated_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        return data_manager.update_entity('City', city_id, updated_data)

    @staticmethod
    def delete(city_id):
        data_manager.delete_entity('City', city_id)

    @staticmethod
    def get_all():
        cities_data = data_manager.get_entities('City')
        cities = []
        for city_data in cities_data:
            city = City(city_data['name'], city_data['country'])
            city.city_id = city_data['city_id']
            city.created_at = city_data['created_at']
            city.updated_at = city_data['updated_at']
            cities.append(city)
        return cities


class Country:
    def __init__(self, name):
        self.country_id = uuid.uuid4().hex
        self.created_at = datetime.now(timezone.utc).isoformat()
        self.updated_at = datetime.now(timezone.utc).isoformat()
        self.name = name
        self.cities = []  # List to store city objects

    def save(self):
        city_ids = [city.city_id for city in self.cities]
        country_data = {
            'country_id': self.country_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'cities': city_ids
        }
        data_manager.create_entity('Country', country_data)

    @staticmethod
    def get_by_id(country_id):
        country_data = data_manager.get_entity_by_id('Country', country_id)
        if country_data:
            country = Country(country_data['name'])
            country.country_id = country_data['country_id']
            country.created_at = country_data['created_at']
            country.updated_at = country_data['updated_at']
            country.cities = [City.get_by_id(city_id) for city_id in country_data['cities']]
            return country
        return None

    @staticmethod
    def update(country_id, updated_data):
        updated_data['updated_at'] = datetime.now(timezone.utc).isoformat()
        return data_manager.update_entity('Country', country_id, updated_data)

    @staticmethod
    def delete(country_id):
        data_manager.delete_entity('Country', country_id)

    @staticmethod
    def get_all():
        countries_data = data_manager.get_entities('Country')
        countries = []
        for country_data in countries_data:
            country = Country(country_data['name'])
            country.country_id = country_data['country_id']
            country.created_at = country_data['created_at']
            country.updated_at = country_data['updated_at']
            country.cities = [City.get_by_id(city_id) for city_id in country_data['cities']]
            countries.append(country)
        return countries

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)
            self.updated_at = datetime.now(timezone.utc).isoformat()
            self.save()

    def remove_city(self, city):
        if city in self.cities:
            self.cities.remove(city)
            self.updated_at = datetime.now(timezone.utc).isoformat()
            self.save()
