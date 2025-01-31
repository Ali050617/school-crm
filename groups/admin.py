from django.contrib import admin
from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'class_leader', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('group_name', 'class_leader__first_name', 'class_leader__last_name')
    autocomplete_fields = ('class_leader',)
    ordering = ('group_name',)
    fieldsets = (
        (None, {
            'fields': ('group_name', 'class_leader'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
