from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    name = models.CharField(verbose_name=_('Name'), max_length=40)
    description = models.CharField(verbose_name=_('Description'), max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
