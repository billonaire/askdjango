from django.conf import settings
from django.db import models


class Post(models.Model):
    #user.post_set.all()을 안하고 shop.models.Post.objects.filter(user=user)를 쓰겠다
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='+' ,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
