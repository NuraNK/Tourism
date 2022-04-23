from django.db import models
from django_quill.fields import QuillField

from accounts.models import User
from base.abstract_model import TimeStampedModel
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(TimeStampedModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Blog(TimeStampedModel):
    category = models.ManyToManyField(Category, related_name='category_blog')
    tag = models.ManyToManyField(Tag, related_name='tag_blog')
    title = models.TextField(null=True, default="")
    paragraph = models.TextField(null=True, default="")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='blog_images/', null=True)
    description = QuillField()
    def __str__(self):
        return self.title

# Blog.objects.filter(category_blog)
class ReviewTotal(TimeStampedModel):
    rate = models.FloatField(default=0.00)
    all = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_totals')


class Commentary(TimeStampedModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    text = models.TextField()
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comment'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


def r(x):
    return round(x * 2.0) / 2.0


class Review(TimeStampedModel):
    # text = models.TextField()
    rate = models.FloatField(validators=[MaxValueValidator(5.0), MinValueValidator(1.0)])
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='reviews')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='reviews')

    def save(self, *args, **kwargs):
        review_total = ReviewTotal.objects.filter(blog=self.blog).first()
        if review_total:
            review_total.total += 1
            review_total.all += self.rate
            review_total.rate = r(review_total.all / review_total.total)
            review_total.save()
        else:
            ReviewTotal.objects.create(rate=self.rate, all=self.rate, total=1, blog=self.blog)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['author', 'blog']
