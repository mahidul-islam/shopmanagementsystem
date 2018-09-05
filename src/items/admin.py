from django.contrib import admin
from items.models import PerWeight, PerPiece, PerLength
from items.forms import CustomPerPieceAdminForm
# for using permalink only...
from django.urls import reverse
from django.utils.html import format_html

class PerPieceAdmin(admin.ModelAdmin):
    fields = ['name', ('price', 'picture'), 'description','slug']
    #must for not creating error
    readonly_fields = ['slug', 'creation_date'] #, 'last_updated'
    form = CustomPerPieceAdminForm
    list_display = ('name', 'price', 'permalink', 'not_in_stock', 'need_to_stock', 'last_updated')
    list_filter = ('not_in_stock', 'need_to_stock', 'last_updated')

    def permalink(self, obj):
        url = reverse("items:show_one_item",
                      kwargs={"slug": obj.slug})
        # Unicode hex b6 is the Pilcrow sign
        return format_html('<a href="{}">{}</a>'.format(url, '\xb6'))


#admin.site.unregister(PerPiece)
admin.site.register(PerPiece, PerPieceAdmin)


class PerLengthAdmin(admin.ModelAdmin):
    pass
admin.site.register(PerLength)


class PerWeightAdmin(admin.ModelAdmin):
    pass
admin.site.register(PerWeight)
