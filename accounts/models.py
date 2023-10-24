from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .manager import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), max_length=100, unique=True,
                              help_text='enter email address')
    mobile_phone = models.CharField(_('Phone number'), max_length=11, unique=True, blank=True)
    full_name = models.CharField(_('Full name'), max_length=100, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    date_of_birth = models.DateField(_('birth day'), blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'mobile_phone', ]
    
    objects = UserManager()
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'