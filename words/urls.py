from django.contrib import admin
from django.urls import path
from .views import get_quiz, get_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', get_quiz, name="quiz"),
    path('result/', get_result, name="result")
]
