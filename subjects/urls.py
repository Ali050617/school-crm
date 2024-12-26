from django.urls import path
from . import views

app_name = 'subjects'


urlpatterns = [
    path('subject_list/', views.subject_list, name='subject_list'),
    path('subject_create/', views.subject_create, name='subject_create'),
    path('subject_update/<int:pk>/', views.subject_update, name='subject_update'),
    path('subject_detail/<int:pk>/', views.subject_detail, name='subject_detail'),
    path('subject_delete/<int:pk>/', views.subject_delete, name='subject_delete')
]