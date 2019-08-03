from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^send_telegram_updates$', views.send_telegram_updates, name='send_telegram_updates'),
]