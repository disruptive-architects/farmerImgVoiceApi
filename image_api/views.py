# image_api/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ImageModel
from .serializers import ImageSerializer

import requests

API_URL = "https://api-inference.huggingface.co/models/ai4bharat/indicwav2vec_v1_bengali"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

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
