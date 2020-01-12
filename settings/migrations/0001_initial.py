# Generated by Django 2.2.7 on 2020-01-12 15:05

from django.db import migrations, models
import datetime
import json
from settings.models import Preference


def load_data(apps, schema_editor):
    f = open('settings/models/json_init/preferences.json', 'r')
    json_data = json.load(f)

    for obj in json_data:
        if obj['name'] == 'preferences':
            for preference in obj['data']:
                preferences = Preference(id=preference['id'], caption=preference['caption'],
                                         created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
                preferences.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.TextField(max_length=128)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('caption', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(load_data),
    ]
