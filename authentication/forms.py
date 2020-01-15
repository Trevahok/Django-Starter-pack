from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import  Profile

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
