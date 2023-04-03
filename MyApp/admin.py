from django.contrib import admin
from .models import Resume


@admin.register(Resume)
class ResumeModel(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'dob', 'gender', 'locality',
        'city', 'pin', 'email', 'state', 'mobile',
        'job_city', 'profile_image', 'my_file'
    ]
