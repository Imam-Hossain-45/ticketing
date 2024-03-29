# Generated by Django 2.2.7 on 2020-02-28 23:58

from django.db import migrations, models
import json
from dh_test.models import Country


def load_data(apps, schema_editor):
    f = open('dh_test/models/json_file/countries.json', 'r')
    json_data = json.load(f)

    for obj in json_data:
        if obj['name'] == 'countries':
            for country in obj['data']:
                c = Country(id=country['id'], name=country['name'], code=country['code'],
                            dial_code=country['dial_code'], currency=country['currency'])
                c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dh_test', '0003_auto_20200218_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, max_length=11, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('dial_code', models.CharField(max_length=255, null=True)),
                ('currency', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(load_data),
    ]
