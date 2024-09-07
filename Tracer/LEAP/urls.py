from django.urls import path
from . import views


urlpatterns = [

    path('leap_dashboard', views.base, name="leap_dashboard"),
    path('employment_rate', views.employment_rate, name='employment_rate'),
    path('industry_distribution', views.industry_distribution, name='industry_distribution'),
    path('job_roles', views.job_roles, name='job_roles'),
    path('time_to_employment', views.time_to_employment, name='time_to_employment'),
    path('faculty-analysis-chart/<str:faculty_code>/', views.faculty_analysis_chart, name='faculty_analysis_chart'),

]
