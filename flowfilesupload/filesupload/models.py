from django.db import models
from django.utils import timezone


class UploadedFile(models.Model):
    files = models.FileField(upload_to='uploads/')
    reading = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(default=timezone.now)
    mpan = models.CharField(max_length=22, default=0)

