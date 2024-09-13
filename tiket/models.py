from datetime import datetime
import uuid
from django.db import models

from user.models import User

# Create your models here.


class Tiket(models.Model):

    class TiketStatus(models.TextChoices):
        OPEN = "OPEN",
        PENDING = "PENDING",
        RESOLVED = "RESOLVED",
        SKIPPED = "SKIPPED",

    class TiketPriority(models.TextChoices):
        LOW = "LOW"
        MEDIUM = "MEDIUM"
        HIGHT = "HIGHT"

    id: uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title: str = models.CharField()
    description: str = models.TextField()
    status: str = models.CharField(
        choices=TiketStatus,
        default=TiketStatus.OPEN,
    )
    created_at: datetime = models.DateTimeField(
        auto_now_add=True, editable=False)
    
    user_id: uuid = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    updated_at: datetime = models.DateTimeField(auto_now=True, editable=False)
    resolved_at: datetime = models.DateTimeField(editable=True, blank=True, null=True)

    def __str__(self):
        return f"Tiket criado em: {self.created_at} - status: {self.status}"