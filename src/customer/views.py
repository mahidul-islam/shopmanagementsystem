from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


class ShowCustomer(LoginRequiredMixin, generic.TemplateView):
    template_name = "customer/show_one_customer.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        customer = get_object_or_404(models.Customer, slug=slug)
        kwargs['show_customer'] = customer
        return super().get(request, *args, **kwargs)
