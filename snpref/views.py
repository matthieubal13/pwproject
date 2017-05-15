# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import csv

# Create your views here.
from .models import Phenotype, SNP, Reference, SNPRefPhen
from django.core.urlresolvers import reverse
# from .forms import SearchForm

def phenotype_list(request):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    phenotypes = Phenotype.objects.all()
    for phenotype in phenotypes:
        phenotype.snp_number = len(SNPRefPhen.objects.filter(phenotype = phenotype))
    return render(request, 'snpref/phenotype_list.html',
    {'phenotypes': phenotypes})


def phenotype_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    phenotype = Phenotype.objects.get(pk = pk)
    snp_refs = SNPRefPhen.objects.filter(phenotype = phenotype)
    return render(request, 'snpref/phenotype_detail.html',
    {'snp_refs' : snp_refs, 'phenotype' : phenotype})


def snp_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    snp = SNP.objects.get(pk = pk)
    snp_refs = SNPRefPhen.objects.filter(snp = snp)
    return render(request, 'snpref/snp_detail.html',
    {'snp_refs' : snp_refs, 'snp' : snp})



def redirect_to_connexion():
    return redirect(reverse('authuser:connection'))
