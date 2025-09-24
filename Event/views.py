from django.shortcuts import render
from django.http import HttpResponse


from .models import Event
# Create your view


def hello(request):
    
    return HttpResponse("<h1> Hello 5twin3 </h1>")



def bonjour(request):
    
    classe="5twin33"
    
    return render(request, 'event/hello.html',{'classroom':classe} )



def listEvent(request):
    
    events =  Event.objects.filter(state=True)
    
    
    
    return render(request, "event/list.html", {'events':events})



def details(request,idEvent):
    
    event =Event.objects.get(id=idEvent)
    
    
    return render(request,"event/details.html", {"e":event})