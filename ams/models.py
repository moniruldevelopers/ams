from django.db import models
from datetime import datetime
import datetime 
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator



class ProgramInfo(models.Model):
    title = models.CharField(max_length=200)    
    program_datetime= models.CharField(max_length=30) # End time
    description = RichTextField()
    banner = models.ImageField(upload_to="program_banners/")
    # max_participants = models.PositiveIntegerField()  
    registrations_count = models.PositiveIntegerField(default=0)  # To track the number of registrations
    max_received = models.PositiveIntegerField(default=30)  # Limit for registrations

    def __str__(self):
        return self.title

    def formatted_time(self):
        # Formatting the date and time to Bangladesh format (e.g., 2:00 PM TO 5:00 PM)
        return f"{self.program_date.strftime('%I:%M %p')} TO {self.program_end_date.strftime('%I:%M %p')}"



class ParticipansInfo(models.Model):
    CLASS_CHOICES = [
        ('Class 5', 'Class 5'),
        ('Class 6', 'Class 6'),
        ('Class 7', 'Class 7'),
        ('Class 8', 'Class 8'),
        ('Class 9', 'Class 9'),
        ('Class 10', 'Class 10'),
        ('Class 11', 'Class 11'),
        ('Class 12', 'Class 12'),
        ('University', 'University'),
    ]

    program = models.ForeignKey(ProgramInfo, on_delete=models.CASCADE, related_name="registrations")
    name = models.CharField(max_length=100)
    whatsapp = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^01[3-9]\d{8}$',
                message="Enter a valid Bangladesh phone number (e.g., 01712345678).",
                code='invalid_phone'
            )
        ]
    )
    email = models.EmailField()
    institute = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    class_level = models.CharField(max_length=20, choices=CLASS_CHOICES)    
    
    def __str__(self):
        return f"{self.name} - {self.program.title}"


class ExportLog(models.Model):
    program = models.ForeignKey(ProgramInfo, on_delete=models.CASCADE, related_name="export_logs")
    export_time = models.DateTimeField(default=now)

    def __str__(self):
        return f"Export Log for {self.program.title} at {self.export_time.strftime('%Y-%m-%d %H:%M:%S')}"
    





class FacebookPage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
