from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher


def teacher_list(request):
    teacher = Teacher.objects.all()
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teachers-list.html', ctx)


def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        science = request.POST.get('science')
        work_experience = request.POST.get('work_experience')
        images = request.FILES.get('images')
        if (first_name and last_name
                and subject and phone_number
                and email and science and
                work_experience and images):
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject,
                phone_number=phone_number,
                email=email,
                science=science,
                work_experience=work_experience,
                images=images
            )
            return redirect('teachers:teacher_list')
    return render(request, 'teachers/teacher-add.html')


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
        science = request.POST.get('science')
        work_experience = request.POST.get('work_experience')
        images = request.FILES.get('images')
        if (first_name and last_name
                and subject and phone_number
                and email and science and
                work_experience and images):
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.subject = subject
            teacher.phone_number = phone_number
            teacher.email = email
            teacher.science = science
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