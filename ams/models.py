from django.db import models
from datetime import datetime
import datetime 
from ckeditor.fields import RichTextField
class ProgramInfo(models.Model):
    title = models.CharField(max_length=200)    
    program_datetime= models.CharField(max_length=30) # End time
    description = RichTextField()
    banner = models.ImageField(upload_to="program_banners/")
    max_participants = models.PositiveIntegerField()  # Max participants allowed
    registrations_count = models.PositiveIntegerField(default=0)  # To track the number of registrations
    max_received = models.PositiveIntegerField(default=30)  # Limit for registrations

    def __str__(self):
        return self.title

    def formatted_time(self):
        # Formatting the date and time to Bangladesh format (e.g., 2:00 PM TO 5:00 PM)
        return f"{self.program_date.strftime('%I:%M %p')} TO {self.program_end_date.strftime('%I:%M %p')}"

class ParticipansInfo(models.Model):
    program = models.ForeignKey(ProgramInfo, on_delete=models.CASCADE, related_name="registrations")
    name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=15)
    email = models.EmailField()
    institute = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.program.title}"
