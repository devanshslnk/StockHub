from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from .choices import UserTypeChoice
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.username=email
        user.save(using=self._db)
        print(user)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)

        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    is_staff =models.BooleanField(default=False)
    contact_number=models.CharField(max_length=13,null=True,unique=True)
    is_superuser =models.BooleanField(default=False)
    user_type=models.CharField(max_length=3,choices=UserTypeChoice.choices,default=UserTypeChoice.CUSTOMER)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


