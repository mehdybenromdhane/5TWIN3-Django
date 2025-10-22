from django.urls import path


from django.contrib.auth.views import LogoutView
from .views import *
urlpatterns = [
    path('login/', login_user , name='login' ),
    path('loginClass/', LoginUser.as_view(), name="loginClass"),
    path('logout/',LogoutView.as_view(), name="logout"),
    
    path('register/', register , name="register")
    
] 