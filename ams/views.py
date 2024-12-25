from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import ParticipantForm

def home(request):
    # Retrieve programs and sort them in descending order by ID, limit to 12
    programs = ProgramInfo.objects.all().order_by('-id')[:12]  # Limit to 12 programs
    return render(request, 'home.html', {'programs': programs})

# Program detail view to show the form
def program_detail(request, program_id):
    program = ProgramInfo.objects.get(id=program_id)
    registrations_count = program.registrations_count
    max_received = program.max_received

    if registrations_count >= max_received:
        messages.warning(request, f"Registration limit reached for {program.title}.")
        return redirect('home')  # Redirect to home if the limit is reached

    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.program = program
            participant.save()

            # Update the registrations count
            program.registrations_count += 1
            program.save()

            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = ParticipantForm()

    return render(request, 'program_detail.html', {'form': form, 'program': program})

def american_corner_list(request):
    pages = FacebookPage.objects.all()  # Alphabetic order
    return render(request, 'american_corner_list.html', {'pages': pages})