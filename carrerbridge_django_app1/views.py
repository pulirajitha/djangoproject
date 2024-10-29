
from django.shortcuts import  render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    return HttpResponse("Welcome To Djnago Tranning at CarrerBridge")

def index(request):
    our_dict = {'insert_CareerBridge':"Career Bridge Djnago Traning Coming From views.py file of Django App!"}
    return render(request,'carrerbridge_django_app1/index.html',context=our_dict)

def student_table(request):
    students = Student.objects.all()
    return render(request, 'carrerbridge_django_app1/student_table.html', {'students':students})

