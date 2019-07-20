from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from .models import *




admin.site.register(Rate)
admin.site.register(CryptoRate)

AdminSite.site_header = "MULTIKASSA"

AdminSite.site_title = "Административный интерфейс MULTIKASSA"

AdminSite.index_title = "Административный интерфейс MULTIKASSA"