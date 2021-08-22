from django.shortcuts import render
from resume.forms import *
from django.contrib import messages

# Create your views here.

def resume(request):
    if request.method =='POST':
        resume = ResumeForm(request.POST. request.FILES)
        if resume.is_valid():
            user = resume.save(commit=False)
            user.save
            messages.success(request, 'Resume done successfully')
    else:
        resume = ResumeForm()
    return render(request, 'public/resume.html', {'new':resume})

 