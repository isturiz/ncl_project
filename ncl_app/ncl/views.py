from django.shortcuts import render
from django.http import HttpResponse

from .models import Representative

def index(request):
    return HttpResponse("Main page")

def home(request):
    return render(request, 'ncl/home/home.html')

def student(request):
    return render(request, 'ncl/student/student.html')


def representative(request):
    return render(request, 'ncl/representative/representative.html')


def detail(request, representative_id):
    representative_list = Representative.objects.all()
    return render(request, "ncl/detail.html", {
        "representative_list": representative_list
    })


def payment(request):
    return render(request, 'ncl/payment/payment.html')