import uuid
from datetime import datetime

class User:
    def __init__(self, email, password, first_name, last_name):
        self.id = uuid.uuid4()
        self.email = email
        self.__password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()  # Creation Date
        self.updated_at = self.created_at  # Update Date
        self.reviews = []

        # Check if email already exists
        for user in User.users:
            if user.email == email:
                raise ValueError("User with this email already exists")

        # If email doesn't exist, add the user to the list
        User.users.append(self)

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.now()

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password
        self.updated_at = datetime.now()

    def __str__(self):
        return f"User: {self.first_name} {self.last_name}, Email: {self.email}"
