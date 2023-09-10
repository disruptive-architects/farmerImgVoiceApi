# image_api/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ImageModel
from .serializers import ImageSerializer

class ImageUploadAPIView(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageListAPIView(APIView):
    def get(self, request, format=None):
        images = ImageModel.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
