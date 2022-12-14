# Generated by Django 4.1.3 on 2022-11-24 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContractModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contract_summa', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'contract',
                'verbose_name_plural': 'contracts',
            },
        ),
        migrations.CreateModel(
            name='MainDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_asked', models.PositiveIntegerField(default=0, verbose_name='soralgan summa')),
                ('money_sent', models.PositiveIntegerField(default=0, verbose_name='tolanishi kerak')),
                ('money_amount', models.PositiveIntegerField(default=0, verbose_name='tolangan summa')),
            ],
            options={
                'verbose_name': 'Asosiy Malumotlar',
                'verbose_name_plural': 'Asosiy Malumotlar',
            },
        ),
        migrations.CreateModel(
            name='RequestStudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_money', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'request_money',
                'verbose_name_plural': 'request_moneys',
            },
        ),
        migrations.CreateModel(
            name='SponsorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('budget', models.IntegerField(default=0, verbose_name='sponsorni qancha puli bor')),
                ('paid_money', models.IntegerField(blank=True, default=0, null=True, verbose_name='nechi pul ajratmoqchi')),
                ('person', models.SmallIntegerField(blank=True, choices=[(0, 'Jismoniy'), (1, 'Yuridik')], null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Yangi'), (2, 'Moderiyatsiyada'), (3, 'Tasdiqlangan'), (4, 'Bekor qilingan')], default=1)),
                ('is_counted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255, unique=True)),
                ('paid_money', models.IntegerField(blank=True, null=True, verbose_name='tolangan pul miqdori')),
                ('student_type', models.IntegerField(choices=[(1, 'bakalavr'), (2, 'magistr')], verbose_name="ta'lim turi")),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='users.contractmodel')),
                ('request_money', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='users.requeststudentmodel', verbose_name='soralgan pul miqdori')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
        migrations.CreateModel(
            name='UniversityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('university', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'university',
                'verbose_name_plural': 'university',
            },
        ),
        migrations.CreateModel(
            name='StudentSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.PositiveIntegerField(verbose_name='olingan pul miqdori')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to='users.sponsormodel', verbose_name='sponsor')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='users.studentmodel', verbose_name='student')),
            ],
            options={
                'verbose_name': 'student and sponsor',
                'verbose_name_plural': 'students and sponsors',
            },
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='users.universitymodel'),
        ),
    ]
