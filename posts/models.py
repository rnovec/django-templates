from django.db import models
from users.models import User
from uuid import uuid4
from .mixins import BaseModelMixin

class Post(BaseModelMixin):
    """Post model."""
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(default="", blank=True, max_length=30)
    description = models.TextField(max_length=255)

    def __str__(self):
        """Return description and username."""
        return self.description


class Comment(BaseModelMixin):
    """Comment model."""
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    message = models.TextField(blank=True, max_length=255)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.message, self.user.username)