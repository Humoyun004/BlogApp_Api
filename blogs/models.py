from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title[:30]}"

