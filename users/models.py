from django.db import models
from rest_framework.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SponsorModel(BaseModel):
    STATUS = [
        (1, 'Yangi'),
        (2, 'Moderiyatsiyada'),
        (3, 'Tasdiqlangan'),
        (4, 'Bekor qilingan')
    ]
    LEGAL_PERSON = 0
    PHYSICAL_PERSON = 1
    PERSON_CHOICES = [(LEGAL_PERSON, 'Jismoniy'), (PHYSICAL_PERSON, 'Yuridik')]
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True)
    budget = models.IntegerField(default=0, verbose_name='sponsorni qancha puli bor')
    paid_money = models.IntegerField(default=0, verbose_name='nechi pul ajratmoqchi', null=True, blank=True)
    person = models.SmallIntegerField(choices=PERSON_CHOICES, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1)
    is_counted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'sponsor'
        verbose_name_plural = 'sponsors'


class ContractModel(BaseModel):
    contract_summa = models.CharField(max_length=12)

    def __str__(self):
        return self.contract_summa

    class Meta:
        verbose_name = 'contract'
        verbose_name_plural = 'contracts'


class UniversityModel(BaseModel):
    university = models.CharField(max_length=100)

    def __str__(self):
        return self.university

    class Meta:
        verbose_name = 'university'
        verbose_name_plural = 'university'


class RequestStudentModel(BaseModel):
    request_money = models.CharField(max_length=12)

    def __str__(self):
        return self.request_money

    class Meta:
        verbose_name = 'request_money'
        verbose_name_plural = 'request_moneys'


class StudentModel(BaseModel):
    EDUCATION_TYPE = [
        (1, 'bakalavr'),
        (2, 'magistr')
    ]
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)
    university = models.ForeignKey(UniversityModel, related_name='student', on_delete=models.CASCADE)
    request_money = models.ForeignKey(RequestStudentModel, related_name='student',
                                      verbose_name='soralgan pul miqdori', on_delete=models.CASCADE,
                                      null=True, blank=True)
    paid_money = models.IntegerField(verbose_name='tolangan pul miqdori',
                                     null=True, blank=True)
    contract = models.ForeignKey(ContractModel, related_name='student', on_delete=models.CASCADE)
    student_type = models.IntegerField(choices=EDUCATION_TYPE, verbose_name="ta'lim turi")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class StudentSponsor(models.Model):
    student = models.ForeignKey(StudentModel, related_name='student', verbose_name='student',
                                on_delete=models.CASCADE)
    sponsor = models.ForeignKey(SponsorModel, related_name='sponsor', verbose_name='sponsor',
                                on_delete=models.CASCADE)
    money = models.PositiveIntegerField(verbose_name='olingan pul miqdori')

    def __str__(self):
        return f"{self.student} {self.sponsor}"

    class Meta:
        verbose_name = 'student and sponsor'
        verbose_name_plural = 'students and sponsors'


# class LinearGraph(models.Model):
#     number_sp = models.PositiveIntegerField(default=0)
#     number_st = models.PositiveIntegerField(default=0)
#     day = models.DateTimeField()
#
#     def __str__(self):
#         return self.day
#
#     class Meta:
#         verbose_name = 'Kunlik Statistika'
#         verbose_name_plural = 'Kunlar Statistikasi'


class MainDatas(models.Model):
    money_asked = models.PositiveIntegerField(default=0, verbose_name='soralgan summa')
    money_sent = models.PositiveIntegerField(default=0, verbose_name='tolanishi kerak')
    money_amount = models.PositiveIntegerField(default=0, verbose_name='tolangan summa')

    def __str__(self):
        return f"So'raldi:  {self.money_asked} Berildi:  {self.money_sent}  Bor:  {self.money_amount}"

    class Meta:
        verbose_name = 'Asosiy Malumotlar'
        verbose_name_plural = 'Asosiy Malumotlar'

    # @receiver(pre_save, sender=StudentSponsor)
    # def check_budget(sender, instance, **kwargs):
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
    # def delete_budget(sender, instance, **kwargs):
    #     student = StudentModel.objects.get(id=instance.student.id)
    #     sponsor = SponsorModel.objects.get(id=instance.sponsor.id)
    #
    #     student.paid_money -= instance.money
    #     sponsor.paid_money -= instance.money
    #     sponsor.budget += instance.money
    #
    #     sponsor.save()
    #     student.save()
