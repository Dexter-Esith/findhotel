# Generated by Django 3.1.5 on 2021-05-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_hotel_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]