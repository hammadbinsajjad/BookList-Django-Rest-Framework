from rest_framework import generics
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer