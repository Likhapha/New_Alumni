# forms.py
from django import forms
from .models import (JobPost, CareerCounseling, AlumniStory, MentorshipProgram,
                     WorkshopEvent, JobApplicationAssistance, InternshipOpportunity)


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'company_name', 'location', 'application_deadline']


class CareerCounselingForm(forms.ModelForm):
    class Meta:
        model = CareerCounseling
        fields = ['counselor_name', 'available_date', 'description']


class AlumniStoryForm(forms.ModelForm):
    class Meta:
        model = AlumniStory
        fields = ['story']


class MentorshipProgramForm(forms.ModelForm):
    class Meta:
        model = MentorshipProgram
        fields = ['mentor_name', 'start_date', 'end_date', 'description']


class WorkshopEventForm(forms.ModelForm):
    class Meta:
        model = WorkshopEvent
        fields = ['title', 'date', 'location', 'description']


class JobApplicationAssistanceForm(forms.ModelForm):
    class Meta:
        model = JobApplicationAssistance
        fields = ['resume_review', 'cover_letter_help', 'interview_preparation', 'description']


class InternshipOpportunityForm(forms.ModelForm):
    class Meta:
        model = InternshipOpportunity
        fields = ['title', 'company_name', 'location', 'description', 'application_deadline']
