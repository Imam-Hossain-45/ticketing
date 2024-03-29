# Generated by Django 2.2.7 on 2020-01-12 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0002_userpreference'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='event/banner/')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('open_gallery', models.BooleanField(blank=True, default=True)),
                ('seat_range', models.IntegerField(blank=True, default=-1)),
                ('paid', models.BooleanField(blank=True, default=False)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('organizer', models.CharField(max_length=60)),
                ('instruction', models.TextField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amenities', models.TextField()),
                ('capacity', models.IntegerField()),
                ('contact_person', models.CharField(max_length=40)),
                ('contact_mobile', models.CharField(max_length=11)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='settings.Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.Event')),
                ('preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.Preference')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='event',
            name='preferences',
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
