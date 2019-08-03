from django.shortcuts import render, redirect
from .models import Rate, CryptoRate, AboutUsSection, ProcessSection, Contacts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.management import call_command
from django.contrib.admin.views.decorators import staff_member_required

def index(request):

    rate = Rate.objects.all()

    crypto_rate = CryptoRate.objects.all()

    about_us = AboutUsSection.objects.all()[0]

    process = ProcessSection.objects.all()

    contacts = Contacts.objects.all()



    context = {
        "rate":rate,
        "crypto_rate":crypto_rate,
        "about":about_us,
        "process": process,
        "contacts": contacts
        
        }

    return render(request, 'rate_page/index.html', context)


@staff_member_required
def send_telegram_updates(request):
    call_command('send_telegram_updates')
    return redirect('/admin/')