# Generated by Django 2.2.7 on 2020-01-12 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_userpreference'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.Address'),
        ),
    ]