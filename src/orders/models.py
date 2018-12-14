from django.db import models
from carts.models import Cart
from my_proj.utils import unique_order_id_generator
from django.db.models.signals import pre_save, post_save

ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('paid','Paid'),
    ('refunded','Refunded'),
    ('shipped','Shipped')
)

class Order(models.Model):
    order_id = models.CharField(max_length = 120, blank = True, null = True)
    # billing profile
    # shipping address
    # billing address
    cart = models.ForeignKey(Cart, on_delete = 'cascade')
    status = models.CharField(max_length=120, default = 'created', choices = ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default = 50, decimal_places = 2, max_digits = 50)
    order_total =  models.DecimalField(default = 0, decimal_places = 2, max_digits = 50)

    def update_total(self):
        # print('updating....')
        cart_total = self.cart.total
        total = cart_total + self.shipping_total
        self.order_total = total
        self.save()

    def __str__(self):
        return self.order_id

def order_pre_save_receiever(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(order_pre_save_receiever, sender=Order)

def post_saved_cart_reciever(sender, instance, created, *args, **kwargs):
    if not created:
        # print('inside...')
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id = cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_saved_cart_reciever, sender = Cart)

def post_saved_order_reciever(sender, instance, created, *args, **kwargs):
    # print('is it there...')
    if created:
        # print('inside...')
        instance.update_total()

post_save.connect(post_saved_order_reciever, sender = Order)
