from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework import filters


class SponsorApplicationView(generics.CreateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorApplicationSerializer
    permission_classes = (AllowAny,)


class SponsorListView(generics.ListAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorProfileSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('full_name',)


class SponsorProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorProfileSerializer
    permission_classes = (IsAuthenticated,)
