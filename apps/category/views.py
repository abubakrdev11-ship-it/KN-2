from django.shortcuts import render
from apps.category.models import Category
from apps.user import permissions
from rest_framework import viewsets
from apps.category.serializers import CategorySerializers


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers