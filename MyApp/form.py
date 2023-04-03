from django import forms
from .models import Resume

GENDER_CHOICE = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITIES = [
    ('Karachi', 'Karachi'),
    ('Lahore', 'Lahore'),
    ('Peshawar', 'Peshawar'),
    ('Quetta', 'Quetta'),
    ('Faisalabad', 'Faisalabad'),
    ('Multan', 'Multan'),
    ('Rawalpindi', 'Rawalpindi'),
    ('Gujranwala', 'Gujranwala'),
    ('Hyderabad', 'Hyderabad'),
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    job_cities = forms.MultipleChoiceField(choices=JOB_CITIES, label='Preferred cities for job',
                                           widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = [
            'name', 'dob', 'gender', 'locality',
            'city', 'pin', 'email', 'state', 'mobile',
            'job_city', 'profile_image', 'my_file'
        ]
        labels = {'name': 'Full Name', 'dob': 'Date of Birth',
                  'pin': 'Pin Code', 'mobile': 'Mobile No.',
                  'email': 'Email ID', 'profile_image': 'Profile Image', 'my_file': 'Document'
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
