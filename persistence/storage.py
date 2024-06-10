class Storage:
    def __init__(self):
        self.data = {
            "users": {},
            "places": {},
            "reviews": {},
            "amenities": {},
            "countries": {
                "US": {"code": "US", "name": "United States"},
                "CA": {"code": "CA", "name": "Canada"},
                # Add more countries as needed
            },
            "cities": {}
        }

    # Other methods...
    
    def get_countries(self):
        return self.data["countries"]

    def get_country(self, code):
        return self.data["countries"].get(code, None)

    def add_city(self, city):
        self.data["cities"][city.id] = city

    def get_cities(self):
        return self.data["cities"].values()

    def get_city(self, city_id):
        return self.data["cities"].get(city_id, None)

    def update_city(self, city):
        self.data["cities"][city.id] = city

    def delete_city(self, city_id):
        if city_id in self.data["cities"]:
            del self.data["cities"][city_id]
