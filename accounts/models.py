from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from datetime import timedelta

class Account(AbstractUser):
    avatar = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
        null=True
    )
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def __str__(self):
        return self.username

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else :
            return True