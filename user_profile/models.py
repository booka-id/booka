from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin ,UserManager


class CostumUserManager(UserManager):
    def _create_user(self, email,password, username, first_name, favorite_book,**extra_fields):
        if not email:
            raise ValueError ("Email salah")
        

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name,favorite_book=favorite_book,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, username=None, first_name=None, favorite_book =None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password,username=username, first_name=first_name, favorite_book=favorite_book,**extra_fields)

    def create_superuser(self, email=None, password=None, username=None, first_name=None,favorite_book =None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password,username=username, first_name=first_name, favorite_book=favorite_book,**extra_fields)
        
class User(AbstractUser, PermissionsMixin):
    profile_pic = models.ImageField(null=True ,blank=True, upload_to='profile_pics/')
    image_url = models.URLField(null=True, blank=True)
    favorite_book = models.JSONField(default=dict, null=True, blank=True)
    wishlist = models.JSONField(default=dict, null=True, blank=True)
    bio = models.TextField(_('bio'), max_length=500, blank=True)
    email= models.EmailField(_('email'),blank=True, default='', unique=True)
    first_name = models.CharField(max_length=255, null=True,blank=True, default='')
    last_name = models.CharField(max_length=255, null=True,blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    objects = CostumUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name
    
# Create your models here.
