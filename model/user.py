import uuid
from datetime import datetime
from model.place import Place
from persistence.data_manager import DataManager

class User:
    data_manager = DataManager()

    def __init__(self, email, password, first_name, last_name):
        """
        Initialize a new User instance.

        Args:
            email (str): User's email address.
            password (str): User's password.
            first_name (str): User's first name.
            last_name (str): User's last name.

        Raises:
            ValueError: If a user with the provided email already exists.
        """
        if User.find_by_email(email):
            raise ValueError("User with this email already exists")

        self.id = str(uuid.uuid4())
        self.email = email
        self._password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()  # Creation Date
        self.updated_at = self.created_at  # Update Date
        self.reviews = []

    def save(self):
        return User.data_manager.save("users", self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
        return User.data_manager.update("users", self)

    def delete(self):
        return User.data_manager.delete("users", self)

    def add_review(self, place_id, content):
        # Check if the user owns the place associated with the review
        place_host_id = User.data_manager.get_place_host_id(place_id)  # Example method to get place host ID
        if place_host_id == self.id:
            raise ValueError("Cannot add review for a place you own")

        review_id = User.data_manager.add_review(self.id, place_id, content)
        self.reviews.append(review_id)
        self.updated_at = datetime.now()
        return User.data_manager.update("users", self)
    
    def add_place(self, name, description, address, city_id, latitude, longitude, num_rooms, num_bathrooms, price_per_night, max_guests):
        new_place = Place(
            name=name,
            description=description,
            address=address,
            city_id=city_id,
            latitude=latitude,
            longitude=longitude,
            host_id=self.id,  # Assigning the user ID as the host ID of the place
            num_rooms=num_rooms,
            num_bathrooms=num_bathrooms,
            price_per_night=price_per_night,
            max_guests=max_guests
        )
        new_place.save()  # Assuming save() method persists the place in the data store
        return new_place

    def get_password(self):
        return self._password

    def set_password(self, new_password):
        self._password = new_password
        self.updated_at = datetime.now()
        return User.data_manager.update("users", self)

    @classmethod
    def find_by_email(cls, email):
        all_users = cls.data_manager.get_all('users')
        for user in all_users:
            if user.email == email:
                return user
        return None

    @classmethod
    def get(cls, user_id):
        return cls.data_manager.get("users", user_id)

    @classmethod
    def get_all(cls):
        return cls.data_manager.get_all('users')

    def __str__(self):
        return f"User: {self.first_name} {self.last_name}, Email: {self.email}"
