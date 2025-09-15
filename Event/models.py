from django.db import models

# Create your models here.

from datetime import datetime

from Person.models import Person

category_list = (('sport','sport'),
                 ('Musique','Musique'),
                 ('Cinema','Cinema')
                 
                 )
class Event(models.Model):
    
    title = models.CharField(max_length=20 )
    description = models.TextField()
    category = models.CharField(choices=category_list, max_length=30)
    state = models.BooleanField(default=True)
    nbr_participants= models.IntegerField(default=0)
    evt_date= models.DateTimeField()
    creation_date=models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images' , null=True)
    
    organisateur = models.ForeignKey(Person,on_delete=models.SET_NULL ,null=True)
    
    def __str__(self):
        
        return self.title
    
    class Meta: 
        constraints = [models.CheckConstraint(check=models.Q(evt_date__gt=datetime.now()), name = "please check the event date")]

    
    

    
