from django.db import models
from django import forms
from django.core.validators import MinLengthValidator

# forms.py에서 이동.
def min_length_3_validator(value):
     if len(value) < 3:
         raise forms.ValidationError('3글자 이상 입력해주세요')
     pass


class Post(models.Model):                       # validators 추가
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    user_agent = models.CharField(max_length=200)
    ip = models.CharField(max_length=15)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)




class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                    choices = (
                       ('A', 'A서버'),
                       ('b', 'B서버'),
                       ('c', 'C서버'),
                    ))
    username = models.CharField(max_length=20, validators=[MinLengthValidator(3)])

    class Meta:
        unique_together = [
            ('server_name', 'username'),
        ]
