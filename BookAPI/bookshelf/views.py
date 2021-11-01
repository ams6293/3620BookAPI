from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class FantasyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Fantasy')
    serializer_class = BookSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Comedy')
    serializer_class = BookSerializer


class DramaViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Drama')
    serializer_class = BookSerializer


class AdventureViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Adventure')
    serializer_class = BookSerializer


class ComingofAgeViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Coming of Age')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Romance')
    serializer_class = BookSerializer


class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Historical Fiction')
    serializer_class = BookSerializer


class HorrorViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Horror')
    serializer_class = BookSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='History')
    serializer_class = BookSerializer


class NonFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(book_category='Non-Fiction')
    serializer_class = BookSerializer