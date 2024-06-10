from persistence.data_manager import DataManager

class City:
    data_manager = DataManager()

    def __init__(self, name, country_code):
        self.id = None
        self.name = name
        self.country_code = country_code
        self.created_at = None
        self.updated_at = None

    def save(self):
        return City.data_manager.save(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return City.data_manager.update(self)

    def delete(self):
        return City.data_manager.delete(self.id, 'city')

    @classmethod
    def get(cls, city_id):
        return City.data_manager.get(city_id, 'city')

    @classmethod
    def get_all(cls):
        return City.data_manager.get_all('city')
