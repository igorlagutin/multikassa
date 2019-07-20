# -*- coding: utf-8 -*-
import urllib.request, json 

from rate_page.models import CryptoRate
from django.core.management.base import BaseCommand


from datetime import datetime





class Command(BaseCommand):

     def handle(self, *args, **options):

          rates = CryptoRate.objects.all()
          for rate in rates:
               api_url = "https://api.binance.com/api/v3/ticker/price?symbol=" + rate.code
               with urllib.request.urlopen(api_url) as url:
                    data = json.loads(url.read().decode())
                    rate.sell = float(data['price'])
                    rate.save()

               
