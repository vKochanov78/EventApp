from django import forms
from .models import ProfileModel, EventModel


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        exclude = ['first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput()
        }


class EventModelForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'
