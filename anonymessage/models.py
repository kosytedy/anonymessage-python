from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider = models.CharField(max_length=15)
    provider_id = models.CharField(max_length=200)
    def __str__(self):
        return self.provider_id


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.message