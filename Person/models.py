from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
def validate_cin(value):
    if len(value) != 8 :
        
        raise ValidationError("Cin must has 8 characters")



def validate_email(value):
    
    if value.endswith('@esprit.tn') ==False:
        
        raise ValidationError("Email must end with @esprit.tn")
    
class Person(AbstractUser):
    
    cin = models.CharField(primary_key=True, max_length=8 ,validators=[validate_cin])
    
    username = models.CharField(max_length=30, unique=True)
    
    email= models.EmailField(max_length=30 , validators=[validate_email])
    
    USERNAME_FIELD="username"
    
    
    class Meta:
        verbose_name= "Person"