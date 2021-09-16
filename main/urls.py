from django.urls import path
from .views import QuestionListAPIView, QuestionCreateAPIView,  AnswerApiView
# from .views import question_list, QuestionDetailView

urlpatterns = [
    path('questions/', QuestionListAPIView.as_view(), name='questions-list'),
    path('question/<int:pk>/', QuestionCreateAPIView.as_view(), name='question-create'),
    path('answer/', AnswerApiView.as_view(), name='answers'),
    # path('questions/', question_list, name='questions'),
    # path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail')
]
