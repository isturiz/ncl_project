from django.urls import path

from .views import home, student, teacher, inscription
from .views import add_student, add_teacher, add_inscription

from .views import representative, add_representative, edit_representative, delete_representative
from .views import course, add_course, edit_course, delete_course
from .views import payment, add_payment

urlpatterns = [

    #ex: ncl/
    path('', home, name='home'),

    #ex: ncl/student
    path('student/', student, name='student'),
    path('student/add/', add_student, name='add_student'),

    #ex: ncl/representative
    path('representative/', representative, name='representative'),
    path('representative/add/', add_representative, name='add_representative'),
    path('representative/edit/', edit_representative, name='edit_representative'),
    path('representative/<int:representative_id>/delete/', delete_representative, name='delete_representative'),
    # path('representative/<int:representative_id>/edit/', edit_representative, name='edit_representative'),

    #ex: ncl/teacher
    path('teacher/', teacher, name='teacher'),
    path('add-teacher/', add_teacher, name='add_teacher'),

    #ex: ncl/payment
    path('payment/', payment, name='payment'),
    path('add-payment/', add_payment, name='add_payment'),


    #ex: ncl/course
    path('course/', course, name='course'),
    path('add-course/', add_course, name='add_course'),
    path('course/<int:course_id>/edit/', edit_course, name='edit_course'),
    path('course/<int:course_id>/delete/', delete_course, name='delete_course'),


    #ex: ncl/inscription
    path('inscription/', inscription, name='inscription'),
    path('add-inscription/', add_inscription, name='add_inscription'),


]
