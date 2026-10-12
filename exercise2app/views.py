from django.shortcuts import render
from .models import Student

def demo(request):
    students = Student.objects.all()
    return render(request, 'demo.html', {'students': students})
