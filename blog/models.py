from django.db import models
from accounts.models import User
from base.abstract_model import TimeStampedModel


class Image(TimeStampedModel):
    file = models.ImageField(upload_to='images/')


class Blog(TimeStampedModel):
    title = models.CharField(max_length=128)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='blog_images/')
    images = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    rating_result = models.FloatField(
        blank=True,
        null=True
    )


class Reviews(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    text = models.TextField()
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )


class RatingStar(TimeStampedModel):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}'


class Rating(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    star = models.ForeignKey(
        RatingStar,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.star}'

    class Meta:
        unique_together = ["user"]


class RatingResult(TimeStampedModel):
    rating = models.IntegerField(default=0)
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.rating}-{self.blog.title}'
