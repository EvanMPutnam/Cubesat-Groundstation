# Generated by Django 3.0 on 2019-12-26 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_view', '0005_dataref_refresh_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataref',
            name='refresh_time',
            field=models.PositiveIntegerField(default=10),
        ),
    ]