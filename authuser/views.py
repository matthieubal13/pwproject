# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from .forms import ConnectionForm
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

def disconnection(request):
    """View for login out.
    This view is not displayed by the browser and redirect automaticly.
    """
    logout(request)
    return redirect(reverse('authuser:connection'))

def connection(request):
    """View for authentication.
    This view displays a form for authentication.
    If correct, it redirect to the site main page.
    """
    if request.user.is_authenticated():
        return redirect_to_phenotype_list()
    error = False
    # Begin of the form.
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                # If the user is correctly authenticated then it is redirected.
                login(request, user)
                return redirect_to_phenotype_list()
            else:
                # Else an error is send to this reloaded page.
                error = True
    else:
        form = ConnectionForm()
    return render(request, 'authuser/connection.html', locals())

def redirect_to_phenotype_list():
    return redirect(reverse('snpref:phenotype_list'))
