# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from datetime import datetime





class Command(BaseCommand):

     def handle(self, *args, **options):
        User.objects.create_superuser('admin','admin@example.com', 'dfns2he2ebhg')