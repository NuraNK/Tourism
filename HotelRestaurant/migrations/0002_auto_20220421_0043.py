# Generated by Django 3.2.12 on 2022-04-20 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelRestaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='date_from',
            field=models.DateField(default=datetime.date(2022, 4, 21)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='date_to',
            field=models.DateField(default=datetime.date(2022, 4, 22)),
        ),
    ]
