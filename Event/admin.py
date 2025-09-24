from django.contrib import admin
from .models import Event,Participants
# Register your models here.




# admin.site.register(Event)




class ParticiaptionInline(admin.TabularInline):
    
    model=Participants
    
    extra=1


def accept_state(ModelAdmin, request, queryset):
    
    queryset.update(state=True)    
    



accept_state.short_description = "change state to true"    
def refuse_state(ModelAdmin, request, queryset):
    
    queryset.update(state=False)    




def changeCategory(ModelAdmin,request,queryset):
    
    queryset.update(category="sport")
    
    
    
@admin.register(Event)
class EventDashboard(admin.ModelAdmin):
    
      list_display=('title','category','description','state','evt_date','organisateur',)  
      
      list_per_page=1
      list_filter=('category','state',)
      
      actions=[accept_state, refuse_state, changeCategory]
      
      inlines=[ParticiaptionInline]
    
    
    
    





admin.site.register(Participants)