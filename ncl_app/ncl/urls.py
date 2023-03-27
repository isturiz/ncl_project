from django.urls import path

from .views import home, student, representative, teacher, payment, course
from .views import add_student, add_representative, add_course, add_teacher

urlpatterns = [

    #ex: ncl/
    path('', home, name='home'),

    #ex: ncl/student
    path('student/', student, name='student'),

    path('add-student/', add_student, name='add_student'),

    #ex: ncl/representative
    path('representative/', representative, name='representative'),
    path('add-representative/', add_representative, name='add_representative'),

    #ex: ncl/teacher
    path('teacher/', teacher, name='teacher'),
    path('add-teacher/', add_teacher, name='add_teacher'),

    #ex: ncl/payment
    path('payment/', payment, name='payment'),

    path('course/', course, name='course'),
    path('add-course/', add_course, name='add_course'),


]
