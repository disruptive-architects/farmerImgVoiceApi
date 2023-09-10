# image_api/models.py

import uuid
from django.db import models


class ImageModel(models.Model):
    unique_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/', default='')
    address = models.CharField(max_length=255, default='')
    mobile_number = models.CharField(max_length=20, default='')
    voice_recording = models.FileField(upload_to='voices/', default='')
    voice_text = models.TextField(default='')
    description = models.TextField(default='')
    upload_date = models.DateTimeField(auto_now_add=True)
