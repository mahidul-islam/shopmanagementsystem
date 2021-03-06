from __future__ import unicode_literals
import uuid
from django.utils import timezone
from django.db import models
from django.conf import settings

class Customer(models.Model):
    name = models.CharField("Customer name", max_length = 100)
    age = models.IntegerField(null=True, blank=True)
    user_sex = (('MALE', 'Male'), ('FEMALE', 'Female'))
    sex = models.CharField(max_length=6, default='Male', choices=user_sex)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    email_address = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    address = models.TextField(null=True, blank=True)
    is_vip = models.BooleanField(default=False)
    made_vip_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   blank = True,
                                   null = True,)
    picture = models.ImageField('Customer photo',
                                upload_to='customer_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description = models.TextField("Short description", max_length=400, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True) #timestamp

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        # TODO: access the logged in user from views.py and pass this to the form just the problelm of items
        # self.updated_by = request.user
        super(Customer, self).save(*args, **kwargs)
