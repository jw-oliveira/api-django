from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

def index(resquest):
    return HttpResponse('Hello World!')

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

