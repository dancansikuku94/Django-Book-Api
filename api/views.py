from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from books.models import    Book
from .serializers import BookSerializer
# Create your views here.


class BookAPIView(generics.ListAPIView):
    querySet=Book.objects.all()
    serializer_class=BookSerializer