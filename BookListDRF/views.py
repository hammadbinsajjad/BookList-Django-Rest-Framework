from rest_framework import generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_xml.renderers import XMLRenderer
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookView(generics.ListCreateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, XMLRenderer]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, XMLRenderer]
    queryset = Book.objects.all()
    serializer_class = BookSerializer