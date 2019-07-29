from django.shortcuts import render
from .models import Rate, CryptoRate, AboutUsSection, ProcessSection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    rate = Rate.objects.all()

    crypto_rate = CryptoRate.objects.all()

    about_us = AboutUsSection.objects.all()[0]

    process = ProcessSection.objects.all()



    context = {
        "rate":rate,
        "crypto_rate":crypto_rate,
        "about":about_us,
        "process": process
        
        }

    return render(request, 'rate_page/index.html', context)