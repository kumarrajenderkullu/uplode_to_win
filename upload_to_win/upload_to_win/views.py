# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from App.models import User
from App.forms import signupform
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def home_view(request):
    # Business Logic
    if request.method == 'GET':
        # display Signup Form
        signup_form = signupform()
        template_name = 'signup.html'
    elif request.method == 'POST':
        # process the data
        signup_form = signupform(request.POST)
        # Validate the Form Dat
        if signup_form.is_valid():
            # Validation Success
            username = signup_form.cleaned_data['username']
            name = signup_form.cleaned_data['name']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            # Save Data to db
            new_user = User(name=name, email=email, password=make_password(password), username=username)
            new_user.save()
            template_name = 'success.html'