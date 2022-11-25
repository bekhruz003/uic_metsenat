from django.shortcuts import render
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

    def check_budget(self):
        if StudentSponsor.student.paid_money >= StudentSponsor.sponsor.budget:
            raise ValidationError('bu summani qosha olmaysiz')
        return StudentSponsor.student.save()

    class MainDatasView(generics.ListAPIView):
        serializer_class = MainDatasSerializer
        permission_classes = (IsAdminUser,)

        def main_datas(self):
            qs = MainDatas.objects.all()
            for date in qs:
                statistic = date.objects.filter().count()
            return statistic

            # @receiver(pre_save, sender=StudentSponsor)
    # def check_budget(self, sender, instance, **kwargs):
    #     student = StudentModel.objects.get(id=instance.student.id)
    #     sponsor = SponsorModel.objects.get(id=instance.sponsor.id)
    #     student_reminder = student.request_money - student.paid_money
    #
    #     if (sponsor.budget >= instance.money and
    #             student.request_money > student.paid_money and
    #             student_reminder >= instance.money):
    #
    #         sponsor.budget -= instance.money
    #         sponsor.paid_money += instance.money
    #         student.paid_money += instance.money
    #         student.save()
    #         sponsor.save()
    #     else:
    #         raise ValidationError(f"{instance.money} summani Qosha olmaysiz")
    #
    # @receiver(pre_delete, sender=StudentSponsor)
    # def delete_budget(self, sender, instance, **kwargs):
    #     student = StudentModel.objects.get(id=instance.student.id)
    #     sponsor = SponsorModel.objects.get(id=instance.sponsor.id)
    #
    #     student.paid_money -= instance.money
    #     sponsor.paid_money -= instance.money
    #     sponsor.budget += instance.money
    #
    #     sponsor.save()
    #     student.save()
