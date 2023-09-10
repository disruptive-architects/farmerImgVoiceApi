# image_api/serializers.py

from rest_framework import serializers
from .models import ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ['unique_id', 'image','address', 'mobile_number', 'voice_recording', 'description', 'upload_date']
