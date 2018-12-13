from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Cart
from products.models import Product

# class cart_home(TemplateView):
#     #print(self.request.session)
#     template_name = 'carts/cart_home.html'


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for product in products:
        total += product.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'carts/cart_home.html', {})

def cart_update(request):
    product_id = request.POST.get('product_id')
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(product_id)
    # TODO: add a try block for product_obj
    product_obj = Product.objects.get(id = product_id)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)

    return redirect("carts:show_cart")
