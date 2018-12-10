from django.shortcuts import render
from products.models import Product
from django.views.generic.list import ListView


class SearchProductView(ListView):
    queryset = Product.objects.all()
    template_name = "search/searched.html"

    # this let us change the queryset below
    def get_queryset(self, *args, **kwargs):
        request = self.request
        dict = request.GET
        query = dict.get('q', None)
        if query is not None:
            return  Product.objects.filter(title__icontains='query')
        return Product.objects.none()
        print(context)
        return context
