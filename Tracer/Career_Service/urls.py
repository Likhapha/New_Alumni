from django.urls import path
from . import views

urlpatterns = [
    path('Career-services', views.career),
    path('career-advice', views.Advice),
    path('my_degree', views.degree),
    path('software', views.software),
    path('business', views.business),
    path('information', views.informatin),
    path('first', views.first_students),
    path('portal', views.career_portal),
    path('Graduates_login', views.Graduates_Login),
    path('new_member', views.new_member),
    path('Making_applications', views.making_appli, name='Making applications'),
    path('interviews_view', views.interviews_view, name='interviews'),
    path("types-of-interviews", views.types_of_interviews, name="types of interviews"),
    path("techniques-of-interviews", views.techniques_of_interviews, name="techniques-of-interviews"),
    path("make-good-first", views.make_good, name="make-good-first")


]