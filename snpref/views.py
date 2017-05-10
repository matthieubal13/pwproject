# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Phenotype

# Create your views here.
def phenotype_list(request):
    phenotypes = Phenotype.objects.all()
    return render(request, 'snpref/phenotype_list.html',
    {'phenotypes': phenotypes})
