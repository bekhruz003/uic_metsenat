from rest_framework import serializers
from .models import SponsorModel, StudentModel, StudentSponsor, MainDatas


# from .tasks import money_management, money_given, money_is_needed


class SponsorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = '__all__'
        read_only_fields = ['paid_money', 'status', 'is_counted']


class SponsorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorModel
        fields = ['full_name', 'phone_number', 'person', 'budget']


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['full_name', 'university', 'contract', 'request_money', 'student_type']


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
        read_only_fields = ['request_money', 'paid_money']


class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = '__all__'


# class LinearGraphSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LinearGraph
#         fields = '__all__'
#         read_only_fields = ['number_sp', 'number_st', 'day']

class MainDatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainDatas
        fields = '__all__'
