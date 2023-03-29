from django.urls import path

from .views import home, student, teacher, payment, course, inscription
from .views import add_student, add_course, add_teacher, add_inscription, add_payment

from .views import representative, add_representative, delete_representative

urlpatterns = [

    #ex: ncl/
    path('', home, name='home'),

    #ex: ncl/student
    path('student/', student, name='student'),
    path('add-student/', add_student, name='add_student'),

    #ex: ncl/representative
    path('representative/', representative, name='representative'),
    path('add-representative/', add_representative, name='add_representative'),
    path('representative/<int:representative_id>/delete/', delete_representative, name='delete_representative'),

    #ex: ncl/teacher
    path('teacher/', teacher, name='teacher'),
    path('add-teacher/', add_teacher, name='add_teacher'),

    #ex: ncl/payment
    path('payment/', payment, name='payment'),
    path('add-payment/', add_payment, name='add_payment'),


    path('course/', course, name='course'),
    path('add-course/', add_course, name='add_course'),

    path('inscription/', inscription, name='inscription'),
    path('add-inscription/', add_inscription, name='add_inscription'),


]
