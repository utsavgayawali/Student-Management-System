from django.shortcuts import render
from .models import Student

# Create your views here.


def student_List(request):
    return render(request,'student_list.html')

def student_Add(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')

        student = Student(name= name,age=age,email=email,address=address)
        student.save()

    return render(request,'student_add.html')

def student_delete(request):
    return render(request,'student_delete.html')