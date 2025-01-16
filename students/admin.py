from django.contrib import admin
from .models import Student
from teachers.models import Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('group', 'first_name', 'last_name', 'birth_date', 'phone_number', 'address', 'images')