
from django.contrib import admin
from .models import *

class ProgramInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'registrations_count', 'max_received')
    
    # Optionally, you can add ordering or filtering to make it easier to manage
   
    search_fields = ('title',)

admin.site.register(ProgramInfo, ProgramInfoAdmin)
admin.site.register(ParticipansInfo)