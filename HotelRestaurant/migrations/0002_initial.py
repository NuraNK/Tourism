# Generated by Django 3.2.12 on 2022-04-30 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('HotelRestaurant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rateroom',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_room', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rateroom',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_room', to='HotelRestaurant.hotels'),
        ),
        migrations.AddField(
            model_name='rateroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_room', to='HotelRestaurant.roomshotel'),
        ),
        migrations.AddField(
            model_name='ratehotels',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_hotel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ratehotels',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_hotel', to='HotelRestaurant.hotels'),
        ),
        migrations.AddField(
            model_name='hotels',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelRestaurant.city'),
        ),
        migrations.AddField(
            model_name='hotels',
            name='gallery',
            field=models.ManyToManyField(blank=True, null=True, related_name='gallery_hotel', to='HotelRestaurant.Gallery'),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HotelRestaurant.hotels'),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_room', to='HotelRestaurant.roomshotel'),
        ),
        migrations.AlterUniqueTogether(
            name='rateroom',
            unique_together={('author', 'room')},
        ),
        migrations.AlterUniqueTogether(
            name='ratehotels',
            unique_together={('author', 'hotel')},
        ),
        migrations.AlterUniqueTogether(
            name='hotelbooking',
            unique_together={('hotel', 'room', 'date_from', 'date_to')},
        ),
    ]
