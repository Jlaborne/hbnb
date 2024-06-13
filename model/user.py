import uuid
from datetime import datetime
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
        return User.data_manager.save(self)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
        return User.data_manager.update(self)

    def delete(self):
        return User.data_manager.delete(self.id, 'user')

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.now()
        return User.data_manager.update(self)

    def get_password(self):
        return self._password

    def set_password(self, new_password):
        self._password = new_password
        self.updated_at = datetime.now()
        return User.data_manager.update(self)

    @classmethod
    def find_by_email(cls, email):
        all_users = cls.data_manager.get_all('user')
        for user in all_users:
            if user.email == email:
                return user
        return None

    @classmethod
    def get(cls, user_id):
        return cls.data_manager.get(user_id, 'user')

    @classmethod
    def get_all(cls):
        return cls.data_manager.get_all('user')

    def __str__(self):
        return f"User: {self.first_name} {self.last_name}, Email: {self.email}"
