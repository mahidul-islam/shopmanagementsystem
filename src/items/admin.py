from django.contrib import admin
from items.models import PerWeight, PerPiece, PerLength

admin.site.register(PerPiece)

admin.site.register(PerLength)

admin.site.register(PerWeight)
