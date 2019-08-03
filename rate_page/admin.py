from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from .models import *


class RateAdmin(admin.ModelAdmin):
	# fields = ('name', 'filters', 'category')

    list_display = ('name','pursage','pursage_delta','sell','sell_delta' )
    list_editable = ('pursage', 'pursage_delta' ,'sell', 'sell_delta')
    ordering = ['id']
    change_list_template = 'admin/rate_page/rate/change_list.html'

class CryptoRateAdmin(admin.ModelAdmin):
    list_display = ('name','sell', 'code')




admin.site.register(Rate, RateAdmin)
admin.site.register(CryptoRate, CryptoRateAdmin)
admin.site.register(AboutUsSection)
admin.site.register(ProcessSection)
admin.site.register(TelegramMessage)
admin.site.register(TelegramButtons)
admin.site.register(Contacts)

AdminSite.site_header = "MULTIKASSA"

AdminSite.site_title = "Административный интерфейс MULTIKASSA"

AdminSite.index_title = "Административный интерфейс MULTIKASSA"