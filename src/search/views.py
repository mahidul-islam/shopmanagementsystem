from django.shortcuts import render
from products.models import Product
from django.views.generic.list import ListView


class SearchProductView(ListView):
    queryset = Product.objects.all()
    template_name = "search/searched.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        print(context)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        dict = request.GET
        query = dict.get('q', None)
        if query is not None:
            return  Product.objects.filter(title__icontains=query)
        return Product.objects.featured()
