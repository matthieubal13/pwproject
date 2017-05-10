# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Phenotype
from .models import SNP

# Create your views here.
def phenotype_list(request):
    phenotypes = Phenotype.objects.all()
    return render(request, 'snpref/phenotype_list.html',
    {'phenotypes': phenotypes})

def snp_list(request):
    snp = SNP.objects.all()
    return render(request, 'snpref/snp_list.html',
    {'snp': snp})
