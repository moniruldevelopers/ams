from django import forms
from .models import ParticipansInfo


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = ParticipansInfo
        fields = ['name', 'whatsapp', 'email', 'institute', 'profession', 'location', 'class_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '11'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'institute': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'class_level': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for choices
            
        }