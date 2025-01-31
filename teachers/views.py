from django.shortcuts import render, redirect, get_object_or_404

from subjects.models import Subject
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', ctx)


def teacher_create(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        work_experience = request.POST.get('work_experience')
        images = request.FILES.get('images')
        print(first_name, last_name, subject_id, phone_number, email, work_experience, images)
        if (first_name and last_name
                and subject_id and phone_number
                and email and
                work_experience and images):
            subject = Subject.objects.get(pk=subject_id)
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject,
                phone_number=phone_number,
                email=email,
                work_experience=work_experience,
                images=images
            )
            return redirect('teachers:teacher_list')
    ctx = {'subjects': subjects}
    return render(request, 'teachers/teacher-add.html', ctx)


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-detail.html', ctx)


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        work_experience = request.POST.get('work_experience')
        images = request.FILES.get('images')
        if (first_name and last_name
                and subject and phone_number
                and email and
                work_experience and images):
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.subject = subject
            teacher.phone_number = phone_number
            teacher.email = email
            teacher.work_experience = work_experience
            teacher.images = images
            teacher.save()
            return redirect(teacher.get_detail_url())
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-add.html', ctx)


def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:teacher_list')
