# Generated by Django 3.2.12 on 2022-04-23 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelRestaurant', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbooking',
            name='user',
        ),
    ]