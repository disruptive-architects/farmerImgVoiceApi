# image_api/urls.py

from django.urls import path
from .views import ImageUploadAPIView, ImageListAPIView

urlpatterns = [
    path('upload/', ImageUploadAPIView.as_view(), name='upload_image_api'),
    path('images/', ImageListAPIView.as_view(), name='image_list_api'),
]
