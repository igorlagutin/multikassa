from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required

from .models import *


class RateAdmin(admin.ModelAdmin):
	# fields = ('name', 'filters', 'category')

    list_display = ('name','pursage','pursage_delta','sell','sell_delta')
    list_editable = ('pursage', 'pursage_delta' ,'sell', 'sell_delta')
    ordering = ['id']
    actions = ['remove_button' ]

    change_list_template = 'admin/rate_page/Rate/change_list.html'

    # def remove_button(self, obj):
    #     return '<a class="button" href="/send_telegram_updates/">Print</a>'
    # remove_button.short_description = 'отправить сообщене в телеграм'
    # remove_button.allow_tags = True

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


# `@staff_member_required
# def export(self, request):

#     call_command('send_telegram_updates')

#     return HttpResponseRedirect(request.META["HTTP_REFERER"])