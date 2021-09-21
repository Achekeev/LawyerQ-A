from rest_framework import serializers
from rest_framework.response import Response

from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('question', 'answer', 'date_answered')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'user', 'question', 'description', 'date_added', 'answers')


