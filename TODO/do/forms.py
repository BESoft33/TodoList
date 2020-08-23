from django import forms
from django.forms import ModelForm
from .models import *


class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = '__all__'
