from django.urls import path

from .views import *
urlpatterns = [
    path('hi/', hello ),
    path('bonjour/', bonjour),
    path('',listEvent , name="listEvent"),
    
    path('details/<int:idEvent>', details , name='detailsEvent'),
    
    path('list/', DispalyEvents.as_view(),name="listClass" ),
    
    path('add/', addEvent, name="addEvent"),
    path('addClass/', AddEvent.as_view(), name="addClass"),
    
    path('update/<int:pk>', UpdateEvent.as_view(), name="updateEvent"),
    
    path('delete/<int:pk>' , DeleteEvent.as_view(), name="deleteEvent"),
    path('join/<int:idEvent>', join , name="join"),
    
    path('cancel/<int:idEvent>',cancel , name='cancel'),
    
    path('generate/', generate_description ,name="generate_description")
]