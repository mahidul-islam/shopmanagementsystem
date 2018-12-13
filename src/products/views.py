from __future__ import unicode_literals
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
#from . import forms
from . import models
from carts.models import Cart

#class ShowItem(LoginRequiredMixin, generic.TemplateView):
#    template_name = "items/show_one_item.html"
#    http_method_names = ['get']

#    def get(self, request, *args, **kwargs):
#        print(kwargs)
#        slug = self.kwargs.get('slug')
#        item = get_object_or_404(models.Product, slug=slug)
#        kwargs['show_item'] = item
#        return super().get(request, *args, **kwargs)

class FeaturedProductDetailView(DetailView):
    queryset = models.Product.objects.featured()
    template_name = 'products/show_one_featured_product.html'


class FeaturedProductListView(ListView):
    queryset = models.Product.objects.featured()
    template_name = 'products/show_all_featured_product.html'



class ProductDetailView(DetailView):
    queryset = models.Product.objects.all()
    #instance = models.Product.objects.get(slug = slug)
    template_name = 'products/show_one_product.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     slug = self.kwargs.get('slug')
    #
    #     # there can be error without try block. add it for multiple object return
    #     instance = get_object_or_404(models.Product, slug=slug)
    #     return instance

class ProductListView(ListView):
    queryset = models.Product.objects.all()
    template_name = "products/show_all_product.html"

    # WE can get and add context in both listview and detailsview with the following method
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     context['abc'] = 123
    #     return context
