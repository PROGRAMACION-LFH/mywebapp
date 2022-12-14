from datetime import datetime
#from django.test
from django.test import TestCase
from .models import Question
from django.utils import timezone

from .models import Question

# Create your tests here.

class  QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
    #def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

