# Generated by Django 3.1.5 on 2021-06-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20210601_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='short_description',
            field=models.TextField(max_length=400),
        ),
    ]