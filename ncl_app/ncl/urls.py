from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),

    path('', views.home, name='home'),

    #ex: ncl/1/
    path("<int:representative_id>/", views.detail, name="detail")
]
