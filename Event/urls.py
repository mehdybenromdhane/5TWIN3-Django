from django.urls import path

from .views import *
urlpatterns = [
    path('hi/', hello ),
    path('bonjour/', bonjour),
    path('',listEvent , name="listEvent"),
    
    path('details/<int:idEvent>', details , name='detailsEvent')
]