# -*- coding: utf-8 -*-
import requests, json 
import telegram
import datetime

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from django.conf import settings
from rate_page.models import CryptoRate, Rate, TelegramMessage, TelegramButtons
from django.core.management.base import BaseCommand


from datetime import datetime


def send_to_telegram(chat_id, message):

    buttons = TelegramButtons.objects.all()
    keyboard = []
    for button in buttons:
        keyboard.append([InlineKeyboardButton(button.button_text, url=button.button_url)])


    bot = telegram.Bot(token=settings.BOT_TOKEN)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, reply_markup=reply_markup)


class Command(BaseCommand):

     def handle(self, *args, **options):


        # date = datetime.today().strftime("%d/%m/%Y")

        telegram_message = TelegramMessage.objects.all()[0].message_text

        message = telegram_message 

        message += '\n\r\n\r'

        crypto_rates = CryptoRate.objects.all()
        rates = Rate.objects.all()

        for rate in rates:
            add_message = "*%s* - купля %d / продажа %d\n\r" % (rate.name, rate.pursage, rate.sell)
            message += add_message

        message += "\n\rКурс криптовалют:\n\r"

        for rate in crypto_rates:
            add_message = "*%s* - %s\n\r" % (rate.name, rate.sell)
            message += add_message


        send_to_telegram(settings.CHAT_ID, message)