from django import forms
from django.forms import CharField


class ResultForm(forms.Form):
    firstname = forms.CharField(label="Enter First Name", max_length=15)
    lastname = forms.CharField(label="Enter Last Name", max_length=15)
    totalmarks = forms.CharField(label="Enter Total Marks", max_length=3)
    grade = forms.CharField(label="Enter your Grade", max_length=2)
    position = forms.CharField(label="Enter your position", max_length=3)
