from __future__ import unicode_literals
from django.views import generic
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
#from . import forms
from . import models


class ShowItem(LoginRequiredMixin, generic.TemplateView):
    template_name = "items/show_one_item.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        print(kwargs)
        slug = self.kwargs.get('slug')
        item = get_object_or_404(models.Product, slug=slug)
        kwargs['show_item'] = item
        return super().get(request, *args, **kwargs)

class ItemListView(ListView):
    queryset = models.Product.objects.all()
    template_name = "items/show_all_item.html"

    # this let us change the queryset below...s
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ItemListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     context['abc'] = 123
    #     return context
