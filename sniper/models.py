from django.db import models

from django.contrib.auth.models import User


class CLSniper(models.Model):
    owner = models.ForeignKey(User, unique=False)
    site = models.TextField(max_length=30)
    query = models.TextField(max_length=140)
    min_price = models.IntegerField(null=True, blank=True)
    max_price = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'sniper'