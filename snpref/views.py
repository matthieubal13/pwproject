# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from .models import Phenotype
from .models import SNP

def phenotype_list(request):
    phenotypes = Phenotype.objects.all()
    return render(request, 'snpref/phenotype_list.html',
    {'phenotypes': phenotypes})

def snp_list(request):
    snp = SNP.objects.all()
    return render(request, 'snpref/snp_list.html',
    {'snp': snp})
