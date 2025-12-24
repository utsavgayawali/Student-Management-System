from django.shortcuts import render,redirect,get_object_or_404
from .models import Student

# Create your views here.


def student_List(request):
    student_info = Student.objects.all()
    return render(request,'student_list.html',{'student_info':student_info})



def student_Add(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')

        student = Student(name= name,age=age,email=email,address=address)
        student.save()
        return redirect('student_List')
    else:
        return render(request,'student_add.html')





def student_Edit(request,student_id):
        student =get_object_or_404(Student,pk=student_id)
        if request.method == 'POST':
            student.name= request.POST.get('name')
            student.email = request.POST.get('email')
            student.age = request.POST.get('age')
            student.address = request.POST.get('address')
            student.save()
            return redirect('student_List')
        else:
            return render(request,'student_add.html',{'student':student})





def student_Delete(request,student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student,pk=student_id)
        student.delete()
        return redirect('student_List')
    else:
        return render(request,'student_delete.html')








