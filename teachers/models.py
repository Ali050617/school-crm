from django.db import models
from subjects.models import Subject
from django.shortcuts import reverse
from teachers.base_models import BaseModel


class Teacher(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    science = models.CharField(max_length=50)
    work_experience = models.PositiveIntegerField(default=0)
    images = models.ImageField(upload_to='photos/', blank=True, null=True)

    def get_detail_url(self):
        return reverse('teachers:teacher_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:teacher_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:teacher_delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.science}"