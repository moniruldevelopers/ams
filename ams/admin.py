
from django.contrib import admin
from .models import *
from django.http import HttpResponse
import csv


@admin.register(FacebookPage)
class FacebookPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')  # Fields to display in the admin list view
    list_filter = ('name',)  # Filters for the list view
    search_fields = ('name', 'url')  # Fields for search functionality
    ordering = ('name',)  # Default ordering by name
#my customizations
admin.site.site_header = "American Corner Barishal"
admin.site.site_title = "American Corner Barishal"
admin.site.index_title = "Welcome to American Corner Barishal"
# Register your models here.

@admin.register(ParticipansInfo)
class ParticipantsInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'whatsapp', 'institute')  # Replace with fields in your model
    search_fields = ('name', 'email', 'whatsapp', 'institute')  # Replace with searchable fields in your model


@admin.register(ProgramInfo)
class ProgramInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'registrations_count', 'max_received')
    search_fields = ('title',)
    actions = ['export_program_participants']

    def export_program_participants(self, request, queryset):
        """Export participants of selected programs."""
        # Handle multiple programs
        if queryset.count() == 1:
            # Use the program title as the filename for single program
            program = queryset.first()
            filename = f"{program.title.replace(' ', '_')}_participants.csv"
        else:
            # Default filename for multiple programs
            filename = "program_participants.csv"

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={filename}'

        writer = csv.writer(response)

        # Write CSV header
        writer.writerow(['Program', 'Name', 'Email', 'WhatsApp', 'Institute', 'Profession', 'Location'])

        # Write data rows for participants in selected programs
        for program in queryset:
            participants = ParticipansInfo.objects.filter(program=program)
            for participant in participants:
                writer.writerow([
                    program.title,
                    participant.name,
                    participant.email,
                    participant.whatsapp,
                    participant.institute,
                    participant.profession,
                    participant.location
                ])

        return response

    export_program_participants.short_description = "Export Participants for Selected Programs to CSV"

