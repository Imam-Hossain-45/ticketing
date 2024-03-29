# Generated by Django 2.2.7 on 2020-02-29 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dh_test', '0004_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profile_picture1', models.ImageField(blank=True, null=True, upload_to='web/test/profile-picture/')),
                ('profile_picture2', models.ImageField(blank=True, null=True, upload_to='web/test/profile-picture/')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dh_test.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LanguageProficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.CharField(blank=True, choices=[('Best', 'Best'), ('Moderate', 'Moderate'), ('Normal', 'Normal'), ('Worst', 'Worst')], max_length=15, null=True)),
                ('user_registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dh_test.UserRegistration')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FoodPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('food', models.CharField(blank=True, max_length=200, null=True)),
                ('user_registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dh_test.UserRegistration')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FnF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('user_registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dh_test.UserRegistration')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
