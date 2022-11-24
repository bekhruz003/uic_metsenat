from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
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


class StudentRegisterView(generics.CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentRegisterSerializer
    permission_classes = (IsAuthenticated,)


class StudentListView(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('full_name',)


class StudentProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAuthenticated,)


class PaidBudgetView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    permission_classes = (IsAuthenticated,)


class MainDatesView(generics.ListAPIView):
    queryset = MainDatas.objects.aggregate().count()
