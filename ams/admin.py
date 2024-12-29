
from django.contrib import admin
from .models import *
from django.http import HttpResponse
import csv


from django.template.loader import render_to_string


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
            # Use the program title as the filename for a single program
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
                # Ensure WhatsApp number is treated as text (to preserve leading zeros)
                whatsapp_number = f"'{str(participant.whatsapp)}"  # Adding a single quote to force Excel to treat it as text
                writer.writerow([
                    program.title,
                    participant.name,
                    participant.email,
                    whatsapp_number,  # Ensure WhatsApp number is handled as a string
                    participant.institute,
                    participant.profession,
                    participant.location
                ])

        return response

    export_program_participants.short_description = "Export Participants for Selected Programs to CSV"











class InterestStudentAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'phone', 'email', 'institute_name', 'class_level')

    # Searchable fields
    search_fields = ('name', 'email', 'phone', 'institute_name')

    # Filters for class_level field
    list_filter = ('class_level',)

    # Export functionality (export to CSV)
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        # Create the HttpResponse object with CSV header
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=interest_students.csv'

        # Create a CSV writer object
        writer = csv.writer(response)
        # Write headers
        writer.writerow(['Name', 'Phone', 'Email', 'Institute Name', 'Class Level'])

        # Write data rows
        for student in queryset:
            # Prefix the phone number with a single quote to ensure it's treated as text in Excel
            phone_number = f"'{str(student.phone)}"  # Single quote to force text format in Excel
            writer.writerow([student.name, phone_number, student.email, student.institute_name, student.class_level])

        return response

    # Define the export action's label
    export_as_csv.short_description = "Export Selected Students as CSV"

# Register the model with the admin
admin.site.register(InterestStudent, InterestStudentAdmin)
