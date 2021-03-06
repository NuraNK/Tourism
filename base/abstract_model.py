from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True, verbose_name="Записан")
    modified = models.DateTimeField(auto_now=True, verbose_name="Изменен")

    class Meta:
        abstract = True


