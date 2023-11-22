from django.contrib import admin
from .models import PoliticiansModel
from .forms import PoliticiansForm

class PoliticiansAdmin(admin.ModelAdmin):
    form = PoliticiansForm
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(PoliticiansModel, PoliticiansAdmin)
# Register your models here.
