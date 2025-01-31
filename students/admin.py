from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'birth_date', 'phone_number')
    list_filter = ('group', 'birth_date')
    search_fields = ('first_name', 'last_name', 'group__group_name', 'phone_number')
    autocomplete_fields = ('group',)
    ordering = ('first_name', 'last_name')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'group', 'birth_date', 'phone_number', 'address', 'images'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
