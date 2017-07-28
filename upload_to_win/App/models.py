# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=40,default='DEFAULT VALUE')
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)