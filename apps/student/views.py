from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from apps.common.responses import StudentResponse

import json

# Create your views here.


def home_page(request):
    msg = "<h3>Welcome to College Manage System</h3>"
    return HttpResponse(msg)


def students_list(request):
    print("Students List")
    students_list = list()
    data = request.GET
    if data.get('year'):
        year = data.get('year')
        students = Student.objects.filter(year=year)
    else:
        students = Student.objects.all()
    for student in students:
        student = StudentResponse.students_entity(src_object=student)
        students_list.append(student)
    students_list = str(students_list)
    return HttpResponse(students_list)


def student_details(request, sid):
    print("students_details")
    msg = "The students"
    student = Student.objects.get(sid=sid)
    student_data = StudentResponse.students_entity(src_object=student)
    student_data = str(student_data)
    return HttpResponse(student_data)
