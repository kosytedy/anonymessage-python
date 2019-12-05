from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    provider = models.CharField(max_length=15)
    provider_id = models.CharField(max_length=200)
    def __str__(self):
        return self.provider_id


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message')
    message = models.TextField(max_length=500)
    date_posted = models.DateTimeField()
    def __str__(self):
        return self.message