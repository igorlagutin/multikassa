from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from .models import *


class RateAdmin(admin.ModelAdmin):
	# fields = ('name', 'filters', 'category')

    list_display = ('name','pursage','sell',)
    list_editable = ('pursage','sell',)
    ordering = ['id']

class CryptoRateAdmin(admin.ModelAdmin):
    list_display = ('name','sell', 'code')




admin.site.register(Rate, RateAdmin)
admin.site.register(CryptoRate, CryptoRateAdmin)

AdminSite.site_header = "MULTIKASSA"

AdminSite.site_title = "Административный интерфейс MULTIKASSA"

AdminSite.index_title = "Административный интерфейс MULTIKASSA"