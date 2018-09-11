import datetime
from django.utils import timezone
from .models import Post
from django.test import TestCase

class QuestionMethod(TestCase):
    def test_was_published(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(created_at = time)
        self.assertEqual(future_post.was_published_recently(), False)

