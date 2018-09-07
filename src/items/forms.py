from django import forms
from items.models import PerWeight, PerPiece, PerLength

class CustomPerPieceAdminForm(forms.ModelForm):
    slug = forms.UUIDField()

    class Meta:
        model = PerPiece
        fields = []
