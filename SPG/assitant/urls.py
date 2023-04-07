from .views import TAView
from django.urls import path

urlpatterns = [
    path('',TAView.as_view()),
]