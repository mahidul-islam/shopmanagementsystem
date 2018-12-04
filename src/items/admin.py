from django.contrib import admin
from items.models import Product
# from items.forms import CustomProductAdminForm
# for using permalink only...
from django.urls import reverse
from django.utils.html import format_html
# for formfield_overrides only...
from django.forms import Textarea
from django.db import models


class ProductAdmin(admin.ModelAdmin):
    #form = CustomProductAdminForm
    fields = [('title', 'slug'),
              ('price', 'not_in_stock', 'need_to_stock'),
              'picture',
              ('creation_date', 'last_updated', 'updated_by'),
              'description']
    #must for not creating error
    readonly_fields = ['slug', 'creation_date', 'last_updated']
    list_display = ('title', 'price', 'permalink', 'not_in_stock', 'need_to_stock', 'last_updated')
    list_filter = ('not_in_stock', 'need_to_stock', 'last_updated')

    def permalink(self, obj):
        url = reverse("items:show_one_item",
                      kwargs={"slug": obj.slug})
        # Unicode hex b6 is the Pilcrow sign
        return format_html('<a href="{}">{}</a>'.format(url, '\xb6'))
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }


#admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)
