from django.urls import path

from . import views

urlpatterns = [

    #ex: ncl/
    path('', views.home, name='home'),

    #ex: ncl/student
    path('student/', views.student, name='student'),
    path('add-student-modal/', views.add_student_modal, name='add_student_modal'),

    #ex: ncl/representative
    path('representative/', views.representative, name='representative'),


    #ex: ncl/teacher
    path('teacher/', views.teacher, name='teacher'),

    #ex: ncl/payment
    path('payment/', views.payment, name='payment'),
    path('add-payment-modal/', views.add_payment_modal, name='add_payment_modal'),

]
