# from django.http import Http404
# from django.shortcuts import render
# from django.views import generic
#
# from .forms import QuestionForm
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import generics


class QuestionListAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerApiView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer



# def question_list(request):
#     questions = Question.objects.all()
#     return render(request, 'questions.html', {'questions': questions})
#
#
# class QuestionDetailView(generic.DetailView):
#     model = Question
#     template_name = 'question-detail.html'
#
#     def detail(request, question_id):
#         try:
#             question = Question.objects.get(pk=question_id)
#         except Question.DoesNotExist:
#             raise Http404("Question does not exist")
#         return render(request, 'question-detail.html', {'question': question})


