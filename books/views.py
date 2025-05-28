from django.shortcuts import render
from .serializers import BookSerializers
from .models import Book
from  rest_framework import  generics

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers