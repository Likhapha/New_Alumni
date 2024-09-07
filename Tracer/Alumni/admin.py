from django.contrib import admin, messages
from django.forms import forms
from django.shortcuts import render
from django.urls import path, reverse
from django.http import HttpResponseRedirect

from .forms import StudentsSurveyForm

from .models import GraduatedStudent, Student
from .models import JobPosting
from .models import EmploymentAnalysis
from .models import StudentsSurvey
from .models import Employer
from .models import InternshipPosting
from .models import ProfessionalDetails
from .models import Survey
from .models import Question
from .models import Option


class csvImportForm(forms.Form):
    csv_upload = forms.FileField()


class Graduands(admin.ModelAdmin):
    list_display = ('student_number', 'names', 'faculty', 'course', 'graduation_year')
    search_fields = ('student_number', 'names')

    def upload_csv(self, request):
        if request.method == "POST":
            form = csvImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES.get("csv_upload")

                if not csv_file or not csv_file.name.endswith('.csv'):
                    messages.warning(request, 'The wrong file type was uploaded')
                    return HttpResponseRedirect(request.path_info)  # Redirect back to the same page

                file_data = csv_file.read().decode("utf-8")
                csv_data = [row.split(",") for row in file_data.strip().split("\n")]

                # Process CSV data and create/update GraduatedStudent objects
                for row in csv_data[1:]:  # Skip the header row
                    GraduatedStudent.objects.update_or_create(
                        names=row[0],
                        course=row[1],
                        student_number=row[2],
                        graduation_year=row[3],
                    )

                messages.success(request, 'CSV file imported successfully.')
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                messages.error(request, 'Form is not valid.')
        else:
            form = csvImportForm()

        data = {"form": form, "csv_data": None}
        return render(request, "admin/csv_upload.html", data)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_csv/', self.upload_csv), ]

        return new_urls + urls


class CurrentStudents(admin.ModelAdmin):
    list_display = ('student_number', 'names', 'faculty', 'course', 'intake_year')
    search_fields = ('student_number', 'names')

    def upload_csv(self, request):
        if request.method == "POST":
            form = csvImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES.get("csv_upload")

                if not csv_file or not csv_file.name.endswith('.csv'):
                    messages.warning(request, 'The wrong file type was uploaded')
                    return HttpResponseRedirect(request.path_info)  # Redirect back to the same page

                file_data = csv_file.read().decode("utf-8")
                csv_data = [row.split(",") for row in file_data.strip().split("\n")]

                # Process CSV data and create/update GraduatedStudent objects
                for row in csv_data[1:]:  # Skip the header row
                    Student.objects.update_or_create(
                        names=row[0],
                        course=row[1],
                        student_number=row[2],
                        intake_year=row[3],
                    )

                messages.success(request, 'CSV file imported successfully.')
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                messages.error(request, 'Form is not valid.')
        else:
            form = csvImportForm()

        data = {"form": form, "csv_data": None}
        return render(request, "admin/csv_upload.html", data)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_csv/', self.upload_csv), ]

        return new_urls + urls


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'faculty', 'course', 'employment_status', 'company_name', 'contacts',
                    'graduation_year', 'email')
    search_fields = ('student_number', 'course', 'faculty')

    def get_faculty(self, course):
        faculty_mapping = {
            "ASSOCIATE DEGREE IN PUBLIC RELATIONS": "FCMB",
            "ASSOCIATE DEGREE IN EVENT MANAGEMENT": "FCTH",
            "ASSOCIATE DEGREE IN BROADCASTING (RADIO & TV)": "FCMB",
            "ASSOCIATE DEGREE IN FILM PRODUCTION": "FCMB",
            "ASSOCIATE DEGREE IN JOURNALISM": "FCMB",
            "ASSOCIATE DEGREE IN BUSINESS MANAGEMENT": "FBG",
            "ASSOCIATE DEGREE IN TOURISM MANAGEMENT": "FCTH",
            "ASSOCIATE DEGREE IN MARKETING": "FBG",
            "ASSOCIATE DEGREE IN RETAIL MANAGEMENT": "FBG",
            "ASSOCIATE DEGREE IN INFORMATION TECHNOLOGY": "FICT",
            "ASSOCIATE DEGREE IN BUSINESS INFORMATION TECHNOLOGY": "FICT",
            "ASSOCIATE DEGREE IN HOTEL MANAGEMENT": "FCTH",
            "ASSOCIATE DEGREE IN INTERNATIONAL TOURISM": "FCTH",
            "ASSOCIATE DEGREE IN MULTIMEDIA & SOFTWARE ENGINEERING": "FICT",
            "ASSOCIATE DEGREE IN GRAPHIC DESIGN": "FDI",
            "ASSOCIATE DEGREE IN ARCHITECTURE TECHNOLOGY": "FABE",
            "ASSOCIATE DEGREE IN CREATIVE ADVERTISING": "FDI",
            "BA IN INTERIOR ARCHITECTURE": "FABE",
            "ASSOCIATE DEGREE IN FASHION & APPAREL DESIGN": "FDI",

            # Add more mappings as needed
        }

        return faculty_mapping.get(course, "Unknown")

    def upload_csv(self, request):
        if request.method == "POST":
            form = csvImportForm(request.POST, request.FILES)

            if form.is_valid():
                graduation_year = request.POST.get('graduation_year')

                csv_file = request.FILES.get("csv_upload")

                if not csv_file or not csv_file.name.endswith('.csv'):
                    messages.warning(request, 'The wrong file type was uploaded')
                    return HttpResponseRedirect(request.path_info)  # Redirect back to the same page

                file_data = csv_file.read().decode("utf-8")
                csv_data = [row.split(",") for row in file_data.strip().split("\n")]

                # Append selected graduation year to each row's graduation_year field
                for row in csv_data[1:]:  # Skip the header row
                    row.append(graduation_year)

                # Process CSV data and create/update GraduatedStudent objects
                for row in csv_data[1:]:  # Skip the header row
                    if len(row) < 6:
                        messages.warning(request, 'One or more rows in the CSV file have fewer columns than expected.')
                        continue  # Skip this row and proceed to the next one

                    try:
                        course = row[0]
                        faculty = self.get_faculty(course)
                        student_number = row[1]

                        # Check if the student number exists in the database
                        obj, created = EmploymentAnalysis.objects.get_or_create(
                            student_number=student_number,
                            defaults={
                                'faculty': faculty,
                                'course': course,
                                'graduation_year': graduation_year,
                                'employment_status': row[4],
                                'company_name': row[5],
                                'email': row[6],
                                'contacts': row[3],
                            }
                        )

                        if not created:
                            # Update the existing object if it's not a new creation
                            obj.faculty = faculty
                            obj.course = course
                            obj.graduation_year = graduation_year
                            obj.employment_status = row[4]
                            obj.company_name = row[5]
                            obj.email = row[6]
                            obj.contacts = row[3]
                            obj.save()

                    except IndexError:
                        messages.error(request, 'Error processing CSV row. Please check the CSV file format.')
                        continue  # Skip this row and proceed to the next one

                messages.success(request, 'CSV file imported successfully.')
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                messages.error(request, 'Form is not valid.')
        else:
            form = csvImportForm()

        data = {"form": form, "csv_data": None}
        return render(request, "admin/csv_upload.html", data)

        # Your other admin configurations

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_csv/', self.upload_csv), ]

        return new_urls + urls


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'workplace_type', 'job_location', 'job_type')
    list_filter = ('workplace_type', 'job_type')
    search_fields = ('job_title', 'company', 'job_location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff and hasattr(request.user, 'employerprofile'):
            employer_profile = request.user.employerprofile
            qs = qs.filter(employer=employer_profile.employer)
        return qs


class StudentsSurveyAdmin(admin.ModelAdmin):
    form = StudentsSurveyForm
    list_display = (
        'faculty', 'degree_level', 'course', 'gender', 'reason', 'program_satisfaction', 'faculty_knowledge',
        'curriculum_satisfaction', 'academic_advisors', 'campus_facilities_satisfaction', 'extracurricular',
        'program_support', 'career_goals', 'career_services', 'comments')
    search_fields = ('faculty', 'course', 'gender')


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'company_email', 'contact_phone', 'address', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['company_name', 'company_email']


@admin.register(InternshipPosting)
class IntershipAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'workplace_type', 'job_location', 'job_type')
    list_filter = ('workplace_type', 'job_type')
    search_fields = ('job_title', 'company', 'job_location')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff and hasattr(request.user, 'employer'):
            employer_profile = request.user.employerprofile
            qs = qs.filter(employer=employer_profile.employer)
        return qs


@admin.register(ProfessionalDetails)
class ProfessionalDetailsAdmin(admin.ModelAdmin):
    list_display = ('employment_status', 'company_name', 'job_position', 'email', 'contacts')
    #list_filter = ('workplace_type', 'job_type')
    search_fields = ('employment_status', 'company_name')


class current_students(admin.ModelAdmin):
    list_display = ('student_number', 'names', 'faculty', 'course',)
    search_fields = ('student_number', 'names')

    def upload_csv(self, request):
        if request.method == "POST":
            form = csvImportForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES.get("csv_upload")

                if not csv_file or not csv_file.name.endswith('.csv'):
                    messages.warning(request, 'The wrong file type was uploaded')
                    return HttpResponseRedirect(request.path_info)  # Redirect back to the same page

                file_data = csv_file.read().decode("utf-8")
                csv_data = [row.split(",") for row in file_data.strip().split("\n")]

                # Process CSV data and create/update GraduatedStudent objects
                for row in csv_data[1:]:  # Skip the header row
                    Student.objects.update_or_create(
                        names=row[0],
                        student_number=row[1],
                        faculty=row[2],
                        course=row[3],
                        email=row[4],
                        contacts=row[5],

                    )

                messages.success(request, 'CSV file imported successfully.')
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                messages.error(request, 'Form is not valid.')
        else:
            form = csvImportForm()

        data = {"form": form, "csv_data": None}
        return render(request, "admin/csv_student.html", data)

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload_csv/', self.upload_csv), ]

        return new_urls + urls


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'deadline', 'target_audience']


#admin.site.register(current_students, Student)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Student, current_students)
admin.site.register(GraduatedStudent, Graduands)
admin.site.register(EmploymentAnalysis, EmploymentAdmin)
admin.site.register(StudentsSurvey, StudentsSurveyAdmin)
