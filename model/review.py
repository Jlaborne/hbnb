import uuid
from datetime import datetime

class Review:
    def __init__(self, user_id, place_id, content):
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.place_id = place_id
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"Review by User {self.user_id} for Place {self.place_id}: {self.content}"
