from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    email = models.EmailField(_('Email'), max_length=100, unique=True, blank=True,
                              help_text='enter emmail address')
    mobile_phone = models.CharField(_('Phone number'), max_length=11, unique=True, blank=True)

