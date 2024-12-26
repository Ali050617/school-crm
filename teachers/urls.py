from django.urls import path
from . import views

app_name = 'teachers'


urlpatterns = [
    path('teacher_list/', views.teacher_list, name='teacher_list'),
    path('teacher_create/', views.teacher_create, name='teacher_create'),
    path('teacher_update/<int:pk>/', views.teacher_update, name='teacher_update'),
    path('teacher_detail/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teacher_delete/<int:pk>/', views.teacher_delete, name='teacher_delete')
]