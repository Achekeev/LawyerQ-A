from django.forms import forms
from .models import Question, Answer


class QuestionForm(forms.Form):
    class Meta:
        models = Question
        fields = ('id', 'user', 'question', 'description')
