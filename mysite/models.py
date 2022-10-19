from django.db import models
from django.conf import settings

class Login(models.Model):
    # username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    number = models.IntegerField()


