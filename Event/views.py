from django.shortcuts import render,redirect
from django.http import HttpResponse


from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from .models import Event,Participants

from Person.models import Person
# Create your view
from .forms import EventForm

from django.urls import reverse_lazy
def hello(request):
    
    return HttpResponse("<h1> Hello 5twin3 </h1>")



def bonjour(request):
    
    classe="5twin33"
    
    return render(request, 'event/hello.html',{'classroom':classe} )



def listEvent(request):
    
    events =  Event.objects.filter(state=True)
    
    
    
    return render(request, "event/list.html", {'events':events})



class DispalyEvents(ListView):
    model=Event
    template_name="event/list.html"
    
    context_object_name="events"
    


def details(request,idEvent):
    
    event =Event.objects.get(id=idEvent)
    
    person= Person.objects.get(cin= 12345678)
    
    participe = Participants.objects.filter(event=event ,person=person)
    
    
    
    if participe:
        btn =True
        
    else:
        btn = False
    
    
    return render(request,"event/details.html", {"e":event ,"btn":btn})



def addEvent(request):
    
    form = EventForm()
    
    if request.method=="POST":
        form = EventForm(request.POST, request.FILES)
        form.save()
        return redirect('listEvent')
    
    return render(request , 'event/add.html', {'form':form})


class AddEvent(CreateView):
    
    model=Event
    form_class=EventForm
    template_name="event/add.html"

    success_url=reverse_lazy('listClass')
    
    

class UpdateEvent(UpdateView):
    model= Event
    form_class=EventForm
    template_name="event/update.html"
    success_url=reverse_lazy('listClass')
    
    

class DeleteEvent(DeleteView):
    model=Event
    template_name="event/delete.html"
    success_url=reverse_lazy('listClass')
    
    
    
def join(request,idEvent):
    
    
    e1 = Event.objects.get(id=idEvent)
    p1 =Person.objects.get(cin = 12345678)
    
    participe = Participants.objects.create(person = p1 , event= e1)
    
    participe.save()
    
    e1.nbr_participants += 1
    
    e1.save()
    
    return redirect('listClass')



def cancel(request,idEvent):
    
    
    e1 = Event.objects.get(id=idEvent)
    p1 =Person.objects.get(cin = 12345678)
    
    participe = Participants.objects.get(person = p1 , event= e1)
    
    participe.delete()
    
    e1.nbr_participants -= 1
    
    e1.save()
    
    return redirect('listClass')