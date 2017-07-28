# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=40,default='DEFAULT VALUE')
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

class SessionToken(models.Model):
	user = models.ForeignKey(User)
	session_token = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True)
	is_valid = models.BooleanField(default=True)

	def create_token(self):
		self.session_token = uuid.uuid4()
