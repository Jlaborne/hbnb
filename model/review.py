import uuid
from datetime import datetime

class Review:
    def __init__(self, rating, comment, user):
        self.id = uuid.uuid4()  # Unique ID
        self.rating = rating
        self.comment = comment
        self.user = user
        self.created_at = datetime.now()  # Creation Date
        self.updated_at = self.created_at  # Update Date
