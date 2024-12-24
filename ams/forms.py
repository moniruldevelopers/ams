from django import forms
from .models import ParticipansInfo

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = ParticipansInfo
        fields = ['name', 'whatsapp', 'email', 'institute', 'profession', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'institute': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
