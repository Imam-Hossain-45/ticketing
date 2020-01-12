# Generated by Django 2.2.7 on 2020-01-12 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('serial_no', models.CharField(max_length=20)),
                ('seat_no', models.CharField(blank=True, max_length=10, null=True)),
                ('unique_id', models.CharField(blank=True, max_length=20, unique=True)),
                ('is_valid', models.BooleanField(blank=True, default=True)),
                ('used', models.BooleanField(blank=True, default=False)),
                ('entry_datetime', models.DateTimeField(blank=True, null=True)),
                ('exit_datetime', models.DateTimeField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.Event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
