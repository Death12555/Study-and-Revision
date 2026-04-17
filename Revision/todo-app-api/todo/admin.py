from django.contrib import admin
from .models import TodoItem

# Register your models here.
class TodoItemAdmin(admin.ModelAdmin):
    """Configuration for the To-Do admin panel."""
    list_display = ['task_name', 'user', 'is_completed', 'created_at', 'updated_at']
    list_filter = ['is_completed', 'user']
    search_fields = ['task_name']
    
    # Ensures timestamps are visible but not editable (since they are auto-generated)
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(TodoItem, TodoItemAdmin)