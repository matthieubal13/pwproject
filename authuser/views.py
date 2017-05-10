# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from .forms import ConnexionForm
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from snpref.views import phenotype_list

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def connexion(request):
    if request.user.is_authenticated():
        return redirect(reverse(phenotype_list))
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse(phenotype_list))
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'authuser/connexion.html', locals())
