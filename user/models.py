import uuid
from datetime import datetime
from django.db import models

# Create your models here.


class User(models.Model):
    id: uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name: str = models.CharField(blank=False)
    email: str = models.EmailField(blank=False, unique=True)
    password: str = models.CharField(max_length=20, blank=False)
    role: str = models.CharField(blank=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)
    

    def __str__(self):
        return f"User - {self.name}"
    
    