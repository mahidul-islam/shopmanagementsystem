from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


class ShowProvider(LoginRequiredMixin, generic.TemplateView):
    template_name = "provider/show_one_provider.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        provider = get_object_or_404(models.Provider, slug=slug)
        kwargs['show_provider'] = provider
        return super().get(request, *args, **kwargs)
