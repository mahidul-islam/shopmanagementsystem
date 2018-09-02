from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings

class BaseItem(models.Model):
    name = models.CharField("Item name", max_length=100)
    price_per_piece = models.IntegerField()
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Item picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description = models.CharField("Short description", max_length=200, blank=True, null=True)

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
