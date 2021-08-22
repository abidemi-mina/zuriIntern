from django.contrib import admin
from resume.models import *
admin.site.site_header='Resume Dashboard'

# Register your models here.
admin.site.register(Resume)