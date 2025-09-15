from django.shortcuts import render
from django.http import HttpResponse

# Create your view


def hello(request):
    
    return HttpResponse("<h1> Hello 5twin3 </h1>")



def bonjour(request):
    
    classe="5twin33"
    
    return render(request, 'event/hello.html',{'classroom':classe} )

