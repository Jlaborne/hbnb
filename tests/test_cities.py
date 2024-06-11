import unittest
from api import app
from model.city import City

class TestCitiesAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_city(self):
        response = self.app.post('/cities', json={"name": "San Francisco", "country_code": "US"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_get_cities(self):
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)

    def test_get_city(self):
        create_response = self.app.post('/cities', json={"name": "Los Angeles", "country_code": "US"})
        city_id = create_response.json['id']
        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json)

    def test_update_city(self):
        create_response = self.app.post('/cities', json={"name": "Seattle", "country_code": "US"})
        city_id = create_response.json['id']
        response = self.app.put(f'/cities/{city_id}', json={"name": "New Seattle"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "New Seattle")

    def test_delete_city(self):
        create_response = self.app.post('/cities', json={"name": "Portland", "country_code": "US"})
        city_id = create_response.json['id']
        response = self.app.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)
        get_response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
