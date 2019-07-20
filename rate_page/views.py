from django.shortcuts import render
from .models import Rate, CryptoRate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    rate = Rate.objects.all()

    crypto_rate = CryptoRate.objects.all()



    context = {
        "rate":rate,
        "crypto_rate":crypto_rate
        
        }

    return render(request, 'rate_page/index.html', context)