# Generated by Django 2.2.7 on 2020-01-12 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
        ('event_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='preference',
            field=models.ManyToManyField(through='event_management.EventPreference', to='settings.Preference'),
        ),
        migrations.AddField(
            model_name='event',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_management.Venue'),
        ),
    ]
