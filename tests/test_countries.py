import unittest
from api import app

class TestCountriesAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)

    def test_get_country(self):
        response = self.app.get('/countries/US')
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json)

    def test_get_invalid_country(self):
        response = self.app.get('/countries/XX')
        self.assertEqual(response.status_code, 404)
