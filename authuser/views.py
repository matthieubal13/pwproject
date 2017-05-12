# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from .forms import ConnectionForm
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

def disconnection(request):
    logout(request)
    return redirect(reverse('authuser:connection'))

def connection(request):
    if request.user.is_authenticated():
        return redirect_to_phenotype_list()
    error = False
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect_to_phenotype_list()
            else:
                error = True
    else:
        form = ConnectionForm()
    return render(request, 'authuser/connection.html', locals())

def redirect_to_phenotype_list():
    return redirect(reverse('snpref:phenotype_list'))
