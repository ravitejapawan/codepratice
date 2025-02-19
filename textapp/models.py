from django.db import models
from django.contrib.auth.models import User

class TextEntry(models.Model):
    text = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

class DeletedTextEntry(models.Model):
    original_id = models.IntegerField()
    text = models.TextField()
    deleted_at = models.DateTimeField(auto_now_add=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
