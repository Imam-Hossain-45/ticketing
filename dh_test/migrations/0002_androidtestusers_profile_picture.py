# Generated by Django 2.2.7 on 2020-02-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dh_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidtestusers',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='android/test/profile-picture/'),
        ),
    ]
