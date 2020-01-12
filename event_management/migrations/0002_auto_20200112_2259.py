# Generated by Django 2.2.7 on 2020-01-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='preferences',
            field=models.ManyToManyField(blank=True, null=True, through='event_management.EventPreference', to='settings.Preference'),
        ),
    ]
