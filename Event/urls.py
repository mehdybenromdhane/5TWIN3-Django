from django.urls import path

from .views import hello,bonjour
urlpatterns = [
    path('hi/', hello ),
    path('bonjour/', bonjour)
]