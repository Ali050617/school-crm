from django.urls import path
from . import views

app_name = 'students'


urlpatterns = [
    path('student_list/', views.student_list, name='student_list'),
    path('student_create/', views.student_create, name='student_create'),
    path('student_update/<int:pk>/', views.student_update, name='student_update'),
    path('student_detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('student_delete/<int:pk>/', views.student_delete, name='student_delete')
]