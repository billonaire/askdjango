import re
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.forms import ValidationError
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):                               #국제화기능 써야됨
    #디폴트뜨면 id값지정해야됨 = 1,2,3,4 등
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # author = models.CharField(max_length=20, settings.AUTH_USER_MODEL)
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    title = models.CharField(max_length=100, verbose_name='제목',
        help_text='셋 중에 하나를 선택하시오')
        # ,
        # choices = (
        #     ('제목1', '제목1 레이블'),
        #     ('제목2', '제목2 레이블'),
        #     ('제목3', '제목3 레이블'),
        # )
    content = models.TextField(verbose_name='내용')

    photo = models.ImageField(blank=True, upload_to='media/%Y/%M/%D')
    photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[Thumbnail(300,300)],
        format='JPEG',
        options={'quality': 60})

    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators=[lnglat_validator],
        help_text='경도,위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    # 주우우우우웅효   detail만드는 즉시 입력할것
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])



class Comment(models.Model):     #post_id로 db에 저장, on_delete필수
    post = models.ForeignKey('Post', on_delete=models.CASCADE,)
    author = models.CharField(max_length=20)
    message = models.TextField()
    content = models.TextField()
    is_blocked = models.BooleanField('노출제한', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
