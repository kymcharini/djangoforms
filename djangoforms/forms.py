from django import forms
from django.forms import CharField


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter First Name", max_length=15)
    lastname = forms.CharField(label="Enter Last Name", max_length=15)
    middlename = forms.CharField(label="Enter Middle Name", max_length=15)
    email = forms.CharField(label="Enter Email Address", max_length=20)
    phonenumber = forms.CharField(label="Enter your Phone Number", max_length=10)
