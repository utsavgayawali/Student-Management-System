from django.shortcuts import render

# Create your views here.


def student_List(request):
    return render(request,'student_list.html')

def student_Add(request):
    return render(request,'student_add.html')

def student_delete(request):
    return render(request,'student_delete.html')