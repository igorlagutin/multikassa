from django.db import models


class Rate(models.Model):

    name = models.CharField(max_length=2048, verbose_name="Имя валюты")
    pursage = models.FloatField(verbose_name="Покупка")
    pursage_delta = models.FloatField(verbose_name="Колебания при покупке", default=0)
    sell = models.FloatField(verbose_name="Продажа")
    sell_delta = models.FloatField(verbose_name="Колебания при продаже", default=0)

    class Meta():
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return str(self.name)


class CryptoRate(models.Model):

    name = models.CharField(max_length=2048, verbose_name="Имя валюты")
    sell = models.FloatField(max_length=2048, verbose_name="Стоимость", default=0)
    code = models.CharField(
        max_length=2048,
        verbose_name="Код",
        help_text='''Проверить код можно по адресу 
            https://api.binance.com/api/v3/ticker/price?symbol= 
            вставьте код после символа =''')

    class Meta():
        verbose_name = "Курс криптовалюты"
        verbose_name_plural = "Курсы криптовалют"

    def __str__(self):
        return str(self.name)


class AboutUsSection(models.Model):
    about_us = models.TextField(verbose_name="Текст О нас")

    class Meta():
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return str("Сюда вводится содержимое раздела 'О нас'")

class ProcessSection(models.Model):
    icon = models.CharField(
        max_length=2048, 
        verbose_name="Иконка",         
        help_text='''код иконки можнопосомтреть тут https://fontawesome.com/icons?d=gallery&s=solid''')
    title = models.CharField(max_length=2048, verbose_name="Заголовок пункта ПРОЦЕСС")
    text = models.TextField(verbose_name="Текст пункта ПРОЦЕСС")

    class Meta():
        verbose_name = "Процесс"
        verbose_name_plural = "Процесс"
        ordering = ['id']

    def __str__(self):
        return str(self.title)

class TelegramMessage(models.Model):
    message_title = CharField(max_length=2048, verbose_name="Заголовок сообщения, никак не влияет на то что будет отправлено, НЕ РЕДАКТИРОВАТЬ")
    message_text = models.TextField(verbose_name="Текст сообщения")
    
    class Meta():
        verbose_name = "Сообщение в телеграм"
        verbose_name_plural = "Сообщение в телеграм"
    
    def __str__(self):
        return str("Текст сообщения в телеграмм")

class TelegramButtons(models.Model):
    button_text = models.CharField(max_length=2048, verbose_name="Текст кнопки") 
    button_url = models.URLField(max_length=2048, verbose_name="URL кнопки", help_text="тут должен быть валидный URL") 

    class Meta():
        verbose_name = "Кнопка"
        verbose_name_plural = "кнопки"
        ordering = ['id']

    def __str__(self):
        return str(self.button_text)