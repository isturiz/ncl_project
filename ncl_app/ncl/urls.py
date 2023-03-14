from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),

    path('', views.home, name='home'),


    #ex: ncl/payment
    path('payment/', views.payment, name='payment'),


    #ex: ncl/student
    path('student/', views.student, name='student'),

    #ex: ncl/student
    path('representative/', views.representative, name='representative'),


    #ex: ncl/1/
    path("<int:representative_id>/", views.detail, name="detail")
]
