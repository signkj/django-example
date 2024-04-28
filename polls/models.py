from datetime import timezone
import datetime
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200) #질문내용
    pub_date = models.DateTimeField("date published") #질문 생성일자

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #질문
    choice_text = models.CharField(max_length=200) #선택지 내용
    votes = models.IntegerField(default=0) #투표수

    def __str__(self):
        return self.choice_text
