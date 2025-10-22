from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth import authenticate,login

from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from .forms import UserRegistration
class LoginUser(LoginView):
     
    def get_success_url(self):
        return reverse_lazy('listEvent')
        

def login_user(request):
    
    
    if request.method == "POST":
       username=  request.POST['username']
       password = request.POST['password']
       
       user= authenticate(request, username = username  , password= password)
    
    
       if user is not None:
           login(request, user)
           
           return redirect('listEvent')
    return render(request,'registration/login.html')



def register(request):
    
    
    form = UserRegistration()
    
    if request.method == "POST":
        form = UserRegistration(request.POST)
        
        if form.is_valid():
           user= form.save()
           login(request,user)
           
           return redirect('listEvent')
    
    return render(request, 'registration/register.html' , {'form':form})