from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class UserModel(AbstractUser):
    pass


class UrlModel(models.Model):
    new_url = models.CharField(max_length=6)
    url = models.URLField(default='')
    count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=CASCADE)

