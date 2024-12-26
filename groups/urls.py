from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('group_list', views.group_list, name='group_list'),
    path('group_create', views.group_create, name='group_create'),
    path('group_update/<int:pk>/', views.group_update, name='group_name'),
    path('group_detail/<int:pk>/', views.group_detail, name='group_detail'),
    path('group_delete/<int:pk>/', views.group_delete, name='group_delete')
]