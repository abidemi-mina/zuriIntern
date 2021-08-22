from django import forms
from resume.models import *
from django.contrib.auth.forms import User



name = 'Abidemi Aminat Adebowale'
print(name)

class ResumeForm(forms.ModelForm):
    Firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Firstname'}))
    Othername = forms.CharField (widget=forms.TextInput(attrs={'placeholder':'Othername'}))
    Surname = forms.CharField (widget=forms.TextInput(attrs={'placeholder':'Surname'}))
    Address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Address'}))
    Experience = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Experience'}))
    Education = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Education'}))
    Skills = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'List your Skills'}))
    hobbies = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Your Hobbies'}))
    phone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Enter Your phone number'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    cv = forms.ImageField(widget=forms.ClearableFileInput(attrs={'placeholder':'Upload your cv'}))
     
    class Meta():
         model = Resume
         fields = '__all__'