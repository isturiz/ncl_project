from django.urls import path

from .views import home, teacher, inscription

from .views import student, add_student, delete_student, edit_student
from .views import representative, edit_representative, delete_representative
from .views import course, edit_course, delete_course
from .views import payment

urlpatterns = [

    #ex: ncl/
    path('', home, name='home'),

    #ex: ncl/student
    path('student/', student, name='student'),
    path('student/add/', add_student, name='add_student'), 
    path('student/<int:id>/edit/', edit_student, name='edit_student'),
    path('student/<int:id>/delete/', delete_student, name='delete_student'),

    #ex: ncl/representative
    path('representative/', representative, name='representative'),
    path('representative/edit/', edit_representative, name='edit_representative'),
    path('representative/<int:representative_id>/delete/', delete_representative, name='delete_representative'),
    # path('representative/<int:representative_id>/edit/', edit_representative, name='edit_representative'),

    #ex: ncl/teacher
    path('teacher/', teacher, name='teacher'),

    #ex: ncl/payment
    path('payment/', payment, name='payment'),

    #ex: ncl/course
    path('course/', course, name='course'),
    path('course/<int:id>/edit/', edit_course, name='edit_course'),
    path('course/<int:id>/delete/', delete_course, name='delete_course'),

    #ex: ncl/inscription
    path('inscription/', inscription, name='inscription'),
]
