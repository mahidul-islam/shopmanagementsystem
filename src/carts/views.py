from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Cart
from products.models import Product
from orders.models import Order
from accounts.forms import LoginFormByMe, LoginForm

# class cart_home(TemplateView):
#     #print(self.request.session)
#     template_name = 'carts/cart_home.html'


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # in this way we can add total in views.py
    # products = cart_obj.products.all()
    # total = 0
    # for product in products:
    #     total += product.price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()
    return render(request, 'carts/cart_home.html', {'cart':cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_id is not None:
        # TODO: add a try block for product_obj
        product_obj = Product.objects.get(id = product_id)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_product_count'] = cart_obj.products.count()
        # print(product_id)
        # print(request.session.get('cart_product_count'))
    return redirect("carts:show_cart")

def checkout_cart(request):
    cart_obj, new_cart_obj = Cart.objects.new_or_get(request)
    if new_cart_obj or cart_obj.products.count() == 0:
        return redirect("carts:show_cart")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart = cart_obj)
    user = request.user
    billing_profile = None
    login_form = LoginForm()

    if user.is_authenticated:
        billing_profile = None
    context = {
        'login_form':login_form,
        'object':order_obj,
        'billing_profile':billing_profile
    }
    return render(request, 'carts/checkout.html', context)
