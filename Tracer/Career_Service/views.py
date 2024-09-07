from django.shortcuts import render


# Create your views here.
def career(request):
    return render(request, 'career/career-service.html')


def Advice(request):
    return render(request, 'career/career_Advice.html')


def degree(request):
    return render(request, 'career/my_degree.html')


def software(request):
    return render(request, 'career/software.html')


def business(request):
    return render(request, 'career/business.html')


def informatin(request):
    return render(request, 'career/information.html')


def first_students(request):
    return render(request, 'career/first_year.html')


def career_portal(request):
    return render(request, 'career/career_portal.html')


def Graduates_Login(request):
    return render(request, 'forms/Graduates_login.html')


def making_appli(request):
    return render(request, 'career/appli_making.html')


def new_member(request):
    return render(request, 'career/new_to_portal.html')


def interviews_view(request):
    return render(request, 'career/interviews.html')


def types_of_interviews(request):
    return render(request, 'career/types_of_interviews.html')


def techniques_of_interviews(require):
    return render(require, 'career/techniques.html')


def make_good(require):
    return render(require, 'career/make_good_first.html')
