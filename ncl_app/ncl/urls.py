from django.urls import path

from .views import home, student, teacher, inscription

from .views import representative, edit_representative, delete_representative
from .views import course, edit_course, delete_course
from .views import payment

urlpatterns = [

    #ex: ncl/
    path('', home, name='home'),

    #ex: ncl/student
    path('student/', student, name='student'),

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
    path('course/<int:course_id>/edit/', edit_course, name='edit_course'),
    path('course/<int:course_id>/delete/', delete_course, name='delete_course'),

    #ex: ncl/inscription
    path('inscription/', inscription, name='inscription'),
]
