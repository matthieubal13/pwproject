# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


# Create your views here.
from .models import Phenotype
from .models import SNP
from django.core.urlresolvers import reverse

def phenotype_list(request):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    phenotypes = Phenotype.objects.all()
    return render(request, 'snpref/phenotype_list.html',
    {'phenotypes': phenotypes})

def phenotype_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    phenotype = Phenotype.objects.get(pk = pk)
    snps = SNP.objects.filter(phenotype = phenotype)
    return render(request, 'snpref/phenotype_detail.html',
    {'phenotype': phenotype, 'snps':snps})

def snp_list(request):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    snp = SNP.objects.all()
    return render(request, 'snpref/snp_list.html',
    {'snp': snp})

def redirect_to_connexion():
    return redirect(reverse('authuser:connection'))
