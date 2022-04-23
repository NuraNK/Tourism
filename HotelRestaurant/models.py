import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import User
from base.abstract_model import TimeStampedModel

class Gallery(TimeStampedModel):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='hotel_images/', null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    city = models.CharField(
        max_length=128,
        unique=True,

    )

    def __str__(self):
        return self.city


class Hotels(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    avatar_hotel = models.ImageField(upload_to='avatar_hotel/')
    gallery = models.ManyToManyField(Gallery, related_name='gallery_hotel', null=True, blank=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
    adress = models.CharField(max_length=128)

    def __str__(self):
        return self.name
# Hotels.objects.filter(reviews_hotel__rate=)

class RoomsHotel(models.Model):
    hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE
    )
    num_room = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    avatar_room = models.ImageField(upload_to='avatar_hotel/')
    gallery = models.ManyToManyField(Gallery, related_name='gallery_room', null=True, blank=True)

    def __str__(self):
        return f'{self.num_room} - цена {self.price}'


class ReviewTotalHotel(TimeStampedModel):
    rate = models.FloatField(default=0.00)
    all = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='hotel_totals')


class ReviewTotal(TimeStampedModel):
    rate = models.FloatField(default=0.00)
    all = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='room_totals')
    room = models.ForeignKey(RoomsHotel, on_delete=models.CASCADE, related_name='room_totals')


def r(x):
    return round(x * 2.0) / 2.0


class RateHotels(TimeStampedModel):
    rate = models.FloatField(validators=[MaxValueValidator(5.0), MinValueValidator(1.0)])
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='reviews_hotel')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='reviews_hotel')

    def save(self, *args, **kwargs):
        review_total = ReviewTotalHotel.objects.filter(hotel=self.hotel).first()
        if review_total:
            review_total.total += 1
            review_total.all += self.rate
            review_total.rate = r(review_total.all / review_total.total)
            review_total.save()
        else:
            ReviewTotalHotel.objects.create(rate=self.rate, all=self.rate, total=1, hotel=self.hotel)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['author', 'hotel']


class RateRoom(TimeStampedModel):
    rate = models.FloatField(validators=[MaxValueValidator(5.0), MinValueValidator(1.0)])
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='reviews_room')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='reviews_room')
    room = models.ForeignKey(RoomsHotel, on_delete=models.CASCADE, related_name='reviews_room')

    def save(self, *args, **kwargs):
        review_total = ReviewTotal.objects.filter(hotel=self.hotel, room=self.room).first()
        if review_total:
            review_total.total += 1
            review_total.all += self.rate
            review_total.rate = r(review_total.all / review_total.total)
            review_total.save()
        else:
            ReviewTotal.objects.create(rate=self.rate, all=self.rate, total=1, hotel=self.hotel, room=self.room)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['author', 'room']


class HotelBooking(TimeStampedModel):
    name = models.CharField(max_length=128)
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE
    # )
    email = models.EmailField()
    hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        RoomsHotel,
        on_delete=models.CASCADE
    )
    CHOISES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    order_num = models.IntegerField()
    guest = models.CharField(max_length=128, choices=CHOISES, null=True)
    children = models.CharField(max_length=128, choices=CHOISES, null=True)
    date_from = models.DateField(default=datetime.date.today())
    date_to = models.DateField(default=datetime.date.today() + datetime.timedelta(1))
    booking = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.date_from}"

    class Meta:
        unique_together = ['hotel', 'room', 'date_from', 'date_to']
