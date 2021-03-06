from logging import setLogRecordFactory
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import  timezone
import  datetime
from django.contrib import admin
# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    # return question object string
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<= now

    @admin.display(boolean=True,ordering='pub_date',description='published recently?',)
    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<=now
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    #return Choice object string 
    def __str__(self):
        return self.choice_text

