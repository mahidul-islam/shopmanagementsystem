from django.urls import path
from . import views

app_name = 'carts'
urlpatterns = [
    path('', views.cart_home, name='show_cart'),
    path('update', views.cart_update, name='update_cart'),
    path('checkout', views.checkout_cart, name='checkout_cart'),

]
