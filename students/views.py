from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from subjects.models import Subject



def home(request):
    return render(request, 'index.html')


def student_list(request):
    student = Student.objects.all()
    ctx = {'students': student}
    return render(request, 'students/students-list.html', ctx)


def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group = request.POST.get('group')
        birth_date = request.POST.get('birth_date')
        images = request.POST.get('images')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        if first_name and last_name and group and birth_date and images and phone_number and address:
            group = get_object_or_404(Subject, group_name=group)
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                group=group,
                birth_date=birth_date,
                images=images,
                phone_number=phone_number,
                address=address
            )
            return redirect('students:student_list')
    return render(request, 'students/student-add.html')


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group = request.POST.get('group')
        birth_date = request.POST.get('birth_date')
        images = request.POST.get('images')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        if first_name and last_name and group and birth_date and images and phone_number and address:
            student.first_name = first_name
            student.last_name = last_name
            student.group = group
            student.birth_date = birth_date
            student.images = images
            student.phone_number = phone_number
            student.address = address
            student.save()
            return redirect(student.get_detail_url())
    ctx = {'students': student}
    return render(request, 'students/student-add.html', ctx)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:student_list')

