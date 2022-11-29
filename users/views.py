from datetime import datetime

from django.shortcuts import render
from django.db.models import Count
from rest_framework.response import Response

from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import filters
from django.core.exceptions import ValidationError


class SponsorApplicationView(generics.CreateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorApplicationSerializer
    permission_classes = (AllowAny,)


class SponsorListView(generics.ListAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorProfileSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('full_name',)


class SponsorProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorProfileSerializer
    permission_classes = (IsAdminUser,)


class StudentRegisterView(generics.CreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentRegisterSerializer
    permission_classes = (IsAdminUser,)


class StudentListView(generics.ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('full_name',)


class StudentProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = (IsAdminUser,)


class PaidBudgetView(generics.ListCreateAPIView):
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    permission_classes = (IsAdminUser,)


class MainDatasView(generics.ListAPIView):
    queryset = MainDatas.objects.all()
    serializer_class = MainDatasSerializer
    permission_classes = (IsAdminUser,)

    def create_datas(self, request):
        yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
        money_amount = SponsorModel.objects.filter(created_at=yesterday).count()
        money_asked = StudentModel.objects.filter(created_at=yesterday).count()
        MainDatas.objects.create(day=yesterday, number_st=money_asked, number_sp=money_amount)
