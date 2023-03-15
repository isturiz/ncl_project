from django.urls import path

from . import views

urlpatterns = [

    #ex: ncl/
    path('', views.home, name='home'),

    #ex: ncl/student
    path('student/', views.student, name='student'),

    #ex: ncl/ ESTA NO SE MUESTRA
    path('representative/', views.representative, name='representative'),


    #ex: ncl/teacher
    path('teacher/', views.teacher, name='teacher'),

    #ex: ncl/payment
    path('payment/', views.payment, name='payment'),

]
