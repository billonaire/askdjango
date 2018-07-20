from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
                                        #이렇게 쓰는게 맞음, 마이그레이션 안해도됨
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
