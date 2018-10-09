from django.db import models

# Create your models here.

from django.conf import setting
from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, BaseUserManager, PermissionsMixin
        )
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created = False, **kwargs):
    """
    Generate a token every time a new account object
    is created.
    """
    if created:
        Token.objects.create(user = instanc)


class AccountManager(BaseUserManager):
    def _create_user(self, email, username, password, image,
            is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a Account with the given email, username and password.
        """
        now = timezone.now()

        if not email:
            raise ValueError('User must have a vaild email address.')

        if not username:
            raise ValueError('The given username must be set.')

        email = self.normalize_email(email)
        try:
            del extra_fields['confirm_password']
        except KeyError:
            pass

        account = self.model(email = email, username = username, image = image,
                is_staff = is_staff, is_active = True, is_superuser = is_superuser,
                last_login = now, date_joined = now, **extra_fields)

        account.set_password(password)
        account.save(using = self._db)
        return account
