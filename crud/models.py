from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

# class Signup(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     email = models.CharField(max_length=200)
#     conditions = models.CharField(max_length=200)
#     category = models.CharField(max_length=200)
#     position = models.CharField(max_length=200)


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an valid username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        # user.is_admin = True
        user.save(using=self._db)
        return user

class Signup(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    firstname=models.CharField(max_length=20, null=True, blank=True)
    lastname=models.CharField(max_length=20, null=True, blank=True)
    gender=models.CharField(max_length=20,null=True, blank=True)
    date_of_birth=models.DateField("date of birth",null=True, blank=True)
    aimage=models.CharField(max_length=200,null=True, blank=True)
    password = models.CharField(max_length=200)
    conditions = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin