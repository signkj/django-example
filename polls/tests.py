from django.test import TestCase
from datetime import timedelta, datetime
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + timedelta(days=30)  # Change datetime to timedelta
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)