from django.contrib import admin
from . import models as provider_model
# for using permalink only...
from django.urls import reverse
from django.utils.html import format_html
# for formfield_overrides only...
from django.forms import Textarea
from django.db import models


class ProviderAdmin(admin.ModelAdmin):
    fields = [('name', 'slug'),
              ('age', 'phone_number', 'picture'),
              ('is_reputed', 'email_address', 'is_vip'),
              'address',
              ('creation_date', 'made_vip_by'),
              'description']
    #must for not creating error
    readonly_fields = ['slug', 'creation_date']
    list_display = ('name', 'permalink', 'is_reputed', 'is_vip', 'made_vip_by', 'creation_date')
    list_filter = ('is_vip', 'is_reputed', 'made_vip_by', 'creation_date')

    def permalink(self, obj):
        url = reverse("provider:show_one_provider",
                      kwargs={"slug": obj.slug})
        # Unicode hex b6 is the Pilcrow sign
        return format_html('<a href="{}">{}</a>'.format(url, '\xb6'))
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':3.5, 'cols':100})},
    }


#admin.site.unregister(PerPiece)
admin.site.register(provider_model.Provider, ProviderAdmin)
