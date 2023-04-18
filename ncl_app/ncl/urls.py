from django.urls import path

from .views import home, teacher, inscription

from .views import student, delete_student
from .views import RepresentativeViews, delete_representative
from .views import course, edit_course, delete_course
from .views import payment

urlpatterns = [

    #ex: ncl/
    path('', home, name='home'),

    #ex: ncl/student

    path('student/', student.index, name='student'), 
    path('student/register/', student.form, name='register_student'), 
    path('student/save/', student.process_form, name='save_student'), 
    path('student/edit/<int:student_id>', student.edit, name='edit_student'),
    path('student/update/<int:student_id>', student.process_edit, name='process_edit'),
    path('student/<int:id>/delete/', delete_student, name='delete_student'),

    path('representative/', RepresentativeViews.index, name='representative'), 
    # path('representative/register/', RepresentativeViews.form, name='register_representative'), 
    # path('representative/save/', RepresentativeViews.process_form, name='save_representative'), 
    # path('representative/edit/<int:representative_id>', RepresentativeViews.edit, name='edit_representative'),
    # path('representative/update/<int:representative_id>', RepresentativeViews.process_edit, name='process_edit'),
    # path('representative/<int:id>/delete/', delete_representative, name='delete_representative'),
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
