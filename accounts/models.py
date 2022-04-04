from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from base.abstract_model import TimeStampedModel

class Role(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "role"

    def __str__(self):
        return f"{self.name}"



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,
                     **extra_fields):
        """
        Create and save a User with given email, and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, TimeStampedModel):
    email = models.EmailField(('email address'), unique=True , blank=True)
    role = models.ForeignKey('accounts.Role',
                             related_name='users',
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             )

    def __str__(self):
        return self.email
