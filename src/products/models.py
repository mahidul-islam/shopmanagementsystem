from __future__ import unicode_literals
import uuid
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse
from django.db.models import Q

from my_proj.utils import unique_order_id_generator


class ProductQuerySet(models.query.QuerySet):
    def active():
        return self.filter(active = True)

class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured = True)
    # def all(self):
    #     return self.get_queryset().active()
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None
    def search(self, query):
        lookups =  (Q(title__icontains=query) |
                    Q(description__icontains=query) |
                    Q(tag__title__icontains=query))
        return self.get_queryset().all().filter(lookups).distinct()

class BaseProduct(models.Model):
    title =             models.CharField("Item name", max_length=100)
    price =             models.DecimalField(decimal_places = 2, max_digits = 50)
    available_stock =   models.PositiveIntegerField(default = 0)
    required_stock =    models.PositiveIntegerField(default = 1)
    not_in_stock =      models.BooleanField(default=True)
    need_to_stock =     models.BooleanField(default=True)
    active =            models.BooleanField(default=True)
    featured =          models.BooleanField(default=False)
    #to add slug useful to the user we use the later method instead of first
    #slug = models.UUIDField(default=uuid.uuid4, blank=True, editable = False)
    slug =              models.SlugField(blank=True, unique=True)

    # Make sure they are nullable
    # or with default values
    picture =           models.ImageField('Item picture',
                                upload_to='item_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    description =       models.TextField("Short description", max_length=400, blank=True, null=True)

    timestamp =     models.DateTimeField(auto_now_add=True) #timestamp
    last_updated =      models.DateTimeField(auto_now=True)

    # Error for uncommenting the thing...
    # Reverse accessor for 'PerLength.created_by' clashes with reverse accessor for 'PerLength.updated_by'
    # ====================================================================================================
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                                on_delete=models.SET_NULL,
    #                                blank = True,
    #                                null = True,)

    updated_by =        models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   blank = True,
                                   null = True,)


    objects = ProductManager()

    def get_absolute_url(self):
        #this is the easy way
        #return '/products/{}/'.format(self.slug)
        reverse('products:show_one_product', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        # TODO: access the logged in user from views.py and pass this to the form
        # self.updated_by = request.user
        super(BaseProduct, self).save(*args, **kwargs)

    class Meta:
        abstract = True

# class PerPiece(BaseItem):
#     #per bottle or thing
#     def __str__(self):_
#         return "{}'s Information". format(self.name)
#
# class PerWeight(BaseItem):
#     def __str__(self):
#         return "{}'s Information". format(self.name)
#
# class PerLength(BaseItem):
#     def __str__(self):
#         return "{}'s  Information". format(self.name)

class Product(BaseProduct):
    def __str__(self):
        return self.title

def product_pre_save_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiever, sender=Product)
