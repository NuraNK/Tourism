from django.db import models
from django_quill.fields import QuillField

from HotelRestaurant.models import City
from accounts.models import User
from base.abstract_model import TimeStampedModel


class Place(TimeStampedModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Gallery(TimeStampedModel):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='tour_images/', null=True)

    def __str__(self):
        return self.name


class Tour(TimeStampedModel):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=models.CASCADE, )
    image = models.ImageField(upload_to='tour_images/')
    place = models.ManyToManyField(Place, related_name='place_tour', null=True, blank=True)
    gallery = models.ManyToManyField(Gallery, related_name='gallery_tour', null=True, blank=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    duration_text = models.CharField(max_length=500)
    price = models.FloatField(default=0.00)
    count = models.IntegerField(default=0)
    short_description = models.TextField()
    description = QuillField(null=True, blank=True)
    image3d = models.ImageField(upload_to='tour_images/', null=True)
    video = models.FileField(upload_to='tour_video/', null=True, blank=True)

    def __str__(self):
        return self.name


class TourOrder(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    count = models.IntegerField(verbose_name="Количество людей")
    confirm = models.BooleanField(default=True, verbose_name="Подтвержден")
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Имя")
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер телефона")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name="Название тура")

    def __str__(self):
        return self.user.email + " --> " + self.tour.name


class UserTour(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=500)
    order = models.ForeignKey(TourOrder, on_delete=models.CASCADE, related_name="ordera")

    def __str__(self):
        return self.name + " --> " + self.order.tour.name
