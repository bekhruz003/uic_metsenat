from django.contrib import admin

from .models import SponsorModel, StudentModel, UniversityModel, ContractModel, RequestStudentModel


@admin.register(SponsorModel)
class SponsorModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'company_name']
    list_display_links = ['full_name', 'company_name']


@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'university']
    list_display_links = ['full_name', 'university']


@admin.register(ContractModel)
class ContractModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'contract_summa']
    list_display_links = ['id', 'contract_summa']


@admin.register(UniversityModel)
class UniversityModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'university']
    list_display_links = ['id', 'university']


@admin.register(RequestStudentModel)
class RequestStudentModelAdmin(admin.ModelAdmin):
    list_display = ['request_money']
    list_display_links = ['request_money']
