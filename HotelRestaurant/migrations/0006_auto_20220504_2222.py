# Generated by Django 3.2.12 on 2022-05-04 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelRestaurant', '0005_alter_rateroom_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='date_from',
            field=models.DateField(default=datetime.date(2022, 5, 4)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='date_to',
            field=models.DateField(default=datetime.date(2022, 5, 5)),
        ),
    ]
