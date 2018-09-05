from __future__ import unicode_literals
import uuid
from django.utils import timezone
from django.db import models
from django.conf import settings

class BaseItem(models.Model):
    name = models.CharField("Item name", max_length=100)
    price = models.IntegerField()
    available_stock = models.IntegerField(default = 0)
    required_stock = models.IntegerField(default = 1)
    not_in_stock = models.BooleanField(default=True)
    need_to_stock = models.BooleanField(default=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Item picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description = models.CharField("Short description", max_length=200, blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True) #timestamp
    last_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class PerPiece(BaseItem):
    #per bottle or thing
    def __str__(self):
        return "{}'s Information". format(self.name)

class PerWeight(BaseItem):
    def __str__(self):
        return "{}'s Information". format(self.name)

class PerLength(BaseItem):
    def __str__(self):
        return "{}'s  Information". format(self.name)
