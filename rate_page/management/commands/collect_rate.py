# -*- coding: utf-8 -*-
import requests, json 

from rate_page.models import CryptoRate
from django.core.management.base import BaseCommand


from datetime import datetime





class Command(BaseCommand):

     def handle(self, *args, **options):

          rates = CryptoRate.objects.all()
          for rate in rates:
                api_url = "https://api.binance.com/api/v3/ticker/price?symbol=" + rate.code
                resp = requests.get(api_url)
                data = json.loads(resp.content.decode())
                rate.sell = float(data['price'])
                rate.save()

               
