from django.db import models


class City(models.Model):
    city = models.CharField(
        max_length=128,
        unique=True,

    )
    def __str__(self):
        return self.city


class HotelRestaurantNum(models.Model):
    num = models.SmallIntegerField()

    def __str__(self):
        return f"{self.num}"


class Restaurants(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True
    )
    description = models.TextField()
    address = models.CharField(max_length=128)
    avatarka = models.ImageField(
        upload_to='avatarka/restaurants/'
    )
    stol_num = models.ForeignKey(
        HotelRestaurantNum,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name


class Hotels(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True
    )
    description = models.TextField()
    address = models.CharField(max_length=128)
    avatarka = models.ImageField(
        upload_to='avatarka/hotels/'
    )

    def __str__(self):
        return self.name

class Booking(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    restaurant = models.ForeignKey(
        Restaurants,
        on_delete=models.CASCADE,
        null=True
    )
    hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE,
        null=True
    )
    phone_number = models.CharField(
        max_length=11,
        # validators=
    )
    reserv_num = models.ForeignKey(
        HotelRestaurantNum,
        on_delete=models.CASCADE,
        null=True
    )
    STATUS = (
        ("Not reserved", "Not reserved"),
        ("Reserved", "Reserved"),
    )
    booking_date = models.DateField()
    booking_status = models.CharField(
        max_length=12,
        choices=STATUS,
        default=False
    )

    def __str__(self):
        if self.hotel is not None:
            return f'{self.hotel} - {self.booking_date}'
        return f'{self.restaurant} - {self.booking_date}'

    class Meta:
        unique_together = [
            "booking_date",
            'reserv_num'
        ]
