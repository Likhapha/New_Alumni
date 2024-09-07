import os

from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render
from io import BytesIO

from Alumni.models import EmploymentAnalysis
from matplotlib import pyplot as plt
from django.conf import settings


def base(request):
    successful_statuses = [
        'EMPLOYED',
        'SELF EMPLOYED',
        'EMPLOYED AND STUDYING',
        'SELF EMPLOYED AND STUDYING',
        'STUDYING AND SELF EMPLOYED',
        'EMPLOYED AND SELF EMPLOYED',
        'SELF EMPLOYED AND EMPLOYED',
    ]

    total_alumni = EmploymentAnalysis.objects.count()
    successful_alumni = EmploymentAnalysis.objects.filter(
        Q(employment_status__in=successful_statuses)
    ).count()

    # Calculate and round the percentage to two decimal places
    percentage_successful = round((successful_alumni / total_alumni) * 100, 2) if total_alumni > 0 else 0.00

    # Aggregate the count of employees for each company and order them by count
    top_companies = EmploymentAnalysis.objects.values('company_name').annotate(
        employee_count=Count('student_number')).order_by('-employee_count')[:3]

    # Combine both contexts into a single dictionary
    context = {
        'top_companies': top_companies,
        'percentage_successful': percentage_successful
    }

    return render(request, 'leap/root_templates/base.html', context)


def employment_rate(request):
    return render(request, 'leap/employment/employment_rate.html', {})


def industry_distribution(request):
    return render(request, 'leap/employment/industry_distribution.html', {})


def job_roles(request):
    return render(request, 'leap/employment/job_roles.html', {})


def time_to_employment(request):
    return render(request, 'leap/employment/time_to_employment.html', {})


def faculty_analysis_chart(request, faculty_code):
    # Retrieve and process data based on the faculty_code
    data = EmploymentAnalysis.objects.filter(faculty=faculty_code, graduation_year__gte=2011)

    # Generate chart
    plt.figure(figsize=(10, 6))

    # Assuming you want to plot the count of alumni per program
    program_counts = data.values('program').annotate(count=Count('id')).order_by('program')
    programs = [item['program'] for item in program_counts]
    counts = [item['count'] for item in program_counts]

    plt.bar(programs, counts)
    plt.xlabel('Program')
    plt.ylabel('Number of Alumni')
    plt.title(f'Alumni Count by Program for Faculty {faculty_code}')
    plt.xticks(rotation=45, ha='right')

    # Save chart to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Define path and ensure directory exists
    chart_path = os.path.join(settings.MEDIA_ROOT, 'charts', f'{faculty_code}_chart.png')
    os.makedirs(os.path.dirname(chart_path), exist_ok=True)

    # Save the chart to a file
    with open(chart_path, 'wb') as f:
        f.write(buf.getvalue())

    # Return chart URL
    return JsonResponse({'chart_url': f'/media/charts/{faculty_code}_chart.png'})
