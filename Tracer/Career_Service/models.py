# models.py
from django.db import models
from django.contrib.auth.models import User


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CareerCounseling(models.Model):
    counselor_name = models.CharField(max_length=255)
    available_date = models.DateTimeField()
    description = models.TextField()
    alumni = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.counselor_name} - {self.available_date}"


class AlumniStory(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumni.username}'s Story"


class MentorshipProgram(models.Model):
    mentor_name = models.CharField(max_length=255)
    mentee = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.mentor_name} mentoring {self.mentee.username}"


class WorkshopEvent(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class JobApplicationAssistance(models.Model):
    alumni = models.ForeignKey(User, on_delete=models.CASCADE)
    resume_review = models.BooleanField(default=False)
    cover_letter_help = models.BooleanField(default=False)
    interview_preparation = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"Assistance for {self.alumni.username}"


class InternshipOpportunity(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()

    def __str__(self):
        return self.title
