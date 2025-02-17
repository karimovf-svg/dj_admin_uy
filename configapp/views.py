from django.shortcuts import render
from .models import Kurs, Student

def kurses(request):
    kurs = Kurs.objects.all()
    context = {
        'kurs': kurs,
        'title': 'Najot talim'
    }
    return render(request, 'Kurs/kurs.html', context)

def studentses(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'title': 'Najot talim'
    }
    return render(request, 'Student/student.html', context)
