from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User,related_name='question_author',on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    content = models.TextField(max_length=30000)
    tags = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)




class Answer(models.Model):
    author = models.ForeignKey(User,related_name='answer_author',on_delete=models.CASCADE)
    question = models.ForeignKey(Question , related_name='answer_question' ,on_delete=models.CASCADE)
    answer = models.TextField(max_length=2000)
    created_at = models.DateTimeField(default=timezone.now)
    


