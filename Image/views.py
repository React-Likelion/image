from django.shortcuts import render
from rest_framework import viewsets

from Image.serializers import ImageSerializer
from .models import Image

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer