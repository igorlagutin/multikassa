from django.db import models



class Rate(models.Model):

    name = models.CharField(max_length=2048, verbose_name="Имя валюты")
    pursage = models.FloatField(verbose_name="Покупка")
    sell = models.FloatField(verbose_name="Продажа")
    code = models.CharField(max_length=2048, verbose_name="Код")

    
    class Meta():
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__ (self):
        return str(self.name)

class CryptoRate(models.Model):

    name = models.CharField(max_length=2048, verbose_name="Имя валюты")
    sell = models.FloatField(max_length=2048, verbose_name="Стоимость")
    code = models.CharField(max_length=2048, verbose_name="Код")

    
    class Meta():
        verbose_name = "Курс криптовалюты"
        verbose_name_plural = "Курсы криптовалют"

    def __str__ (self):
        return str(self.name)


