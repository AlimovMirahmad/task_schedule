from django.urls import path
from .views import ServiceAPIView, TaskCreateAPIView

urlpatterns = [
    path('register/', ServiceAPIView.as_view()),
    path('taskcreat/', TaskCreateAPIView.as_view()),
    ]
