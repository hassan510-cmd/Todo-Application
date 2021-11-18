from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# # Create your models here.
#
class UserProfileManager(BaseUserManager):
    """help django work with our custom user model"""
    def create_user(self,name,email,password=None):
        """create new user"""
        if not email:
            raise ValueError('user must have email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,name,email,password=None):
        user=self.create_user(name,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
#
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """this is the user profile model"""
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get user full name"""
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email
#
#
#     # def __repr__(self):
#     #     return str({
#     #         'id':self.id,
#     #         'name':self.name,
#     #         'email':self.email
#     #     })