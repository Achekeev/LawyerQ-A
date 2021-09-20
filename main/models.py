from django.db import models
from django.utils import timezone


class Question(models.Model):
    user = models.CharField(max_length=255, default='Anonymous')
    question = models.CharField(max_length=1000)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    date_answered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.question




