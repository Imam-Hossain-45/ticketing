# Generated by Django 2.2.7 on 2020-01-13 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0004_auto_20200112_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
