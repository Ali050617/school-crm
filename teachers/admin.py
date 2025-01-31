from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject', 'email', 'phone_number', 'work_experience')
    list_filter = ('subject', 'work_experience')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'subject__name')
    autocomplete_fields = ('subject',)
    ordering = ('first_name', 'last_name')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'subject', 'phone_number', 'email', 'work_experience', 'images'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
