# stickynotes/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    # 🔑 FIX: Added the missing field with auto_now=True
    updated_at = models.DateTimeField(auto_now=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    # Optional owner for now (login not yet implemented)
    owner = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='notes'
    )

    def __str__(self):
        return self.title
