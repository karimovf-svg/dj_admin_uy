from django.shortcuts import render
from .models import Kurs, Student

def kurses(request):
    kurs = Kurs.objects.all()
    context = {
        'news': kurs,
        'title': 'Najot talim'
    }
    return render(request, 'Kurs/kurs.html', context)

def studentses(request):
    students = Student.objects.all()
    context = {
        'news': students,
        'title': 'Najot talim'
    }
    return render(request, 'Student/student.html', context)
