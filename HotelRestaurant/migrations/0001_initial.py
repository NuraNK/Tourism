# Generated by Django 3.2.12 on 2022-04-30 18:37

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Записан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(null=True, upload_to='hotel_images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Записан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('order_num', models.IntegerField()),
                ('guest', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=128, null=True)),
                ('children', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=128, null=True)),
                ('date_from', models.DateField(default=datetime.date(2022, 5, 1))),
                ('date_to', models.DateField(default=datetime.date(2022, 5, 2))),
                ('booking', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('avatar_hotel', models.ImageField(upload_to='avatar_hotel/')),
                ('adress', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='RateHotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Записан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='RateRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Записан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('rate', models.FloatField(validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(1.0)])),
            ],
        ),
        migrations.CreateModel(
            name='RoomsHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_room', models.IntegerField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('avatar_room', models.ImageField(upload_to='avatar_hotel/')),
                ('gallery', models.ManyToManyField(blank=True, null=True, related_name='gallery_room', to='HotelRestaurant.Gallery')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelRestaurant.hotels')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewTotalHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Записан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('rate', models.IntegerField(default=0)),
                ('all', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_totals', to='HotelRestaurant.hotels')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReviewTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Записан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('rate', models.FloatField(default=0.0)),
                ('all', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_totals', to='HotelRestaurant.hotels')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_totals', to='HotelRestaurant.roomshotel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
