from django.contrib import admin
from .models import Blog, Review, ReviewTotal, Category, Tag, Commentary

# Register your models here.
# admin.site.register(Commentary)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Commentary)
admin.site.register(Review)
admin.site.register(ReviewTotal)
admin.site.register(Category)
