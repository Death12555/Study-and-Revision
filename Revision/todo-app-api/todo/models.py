from django.db import models
from django.conf import settings

# Create your models here.
class TodoItem(models.Model):
    """Model for a to-do list item"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    # 'auto_now_add' sets the time only when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)

    # 'auto_now' updates the time every time the object is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a string representation of the task"""
        return self.task_name
