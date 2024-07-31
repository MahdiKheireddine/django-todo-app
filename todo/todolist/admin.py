from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_complete', 'created')
    readonly_fields = ('created',)  # Make the field read-only in the admin form

admin.site.register(Task, TaskAdmin)
