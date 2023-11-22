from django import forms
from .models import PoliticiansModel

class PoliticiansForm(forms.Form):
    name_uz = forms.CharField()
    name_en = forms.CharField()
    name_ru = forms.CharField()

    position_uz = forms.CharField()
    position_en = forms.CharField()
    position_ru = forms.CharField()

    class Meta:
        model = PoliticiansModel
        exclude = ('name',)

