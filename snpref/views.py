# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import csv

# Create your views here.
from .models import Phenotype, SNP, Reference, SNPRefPhen
from django.core.urlresolvers import reverse
from .forms import SearchForm

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

def snp_list(request):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    snps = SNP.objects.all()
    for snp in snps:
        snp.ref = SNPRefPhen.objects.filter(snp = snp)
    return render(request, 'snpref/snp_list.html',
    {'snps': snps})


def snp_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    snp = SNP.objects.get(pk = pk)
    snp_refs = SNPRefPhen.objects.filter(snp = snp)
    return render(request, 'snpref/snp_detail.html',
    {'snp_refs' : snp_refs, 'snp' : snp})

def snp_search(request):
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            search_phen = form.cleaned_data["phenotypes"]
            if not search_phen:
                phenotypes = Phenotype.objects.all()
            else:
                phenotypes = set()
                search_phen = search_phen.split(",")
                for sp in search_phen:
                    sp = sp.strip(" ").capitalize()
                    phenotype = Phenotype.objects.filter(trait = sp)
                    if phenotype:
                        phenotype = phenotype[0]
                        phenotypes.add(phenotype)
            if not search:
                snps_all = SNP.objects.all()
                snps = set()
                for snp in snps_all:
                    allowed = False
                    snp_ref = SNPRefPhen.objects.filter(snp = snp)
                    if not snp_ref:
                        continue
                    for phenotype in phenotypes:
                        if phenotype.trait == snp_ref[0].phenotype.trait:
                            allowed = True
                            snp.ref = snp_ref[0].ref
                    if allowed:
                        snps.add(snp)
            else:
                snps = set()
                search = search.split(",")
                for s in search:
                    s = s.strip(" ")
                    snp = SNP.objects.filter(rs_id = s)
                    if snp:
                        allowed = False
                        snp = snp[0]
                        snp_ref = SNPRefPhen.objects.filter(snp = snp)
                        if not snp_ref:
                            continue
                        for phenotype in phenotypes:
                            if phenotype.trait == snp_ref[0].phenotype.trait:
                                allowed = True
                                snp.ref = snp_ref[0].ref

                        if allowed:
                            snps.add(snp)
    else:
        form = SearchForm()
    return render(request, 'snpref/search.html', locals())

def get_clean_search(search, phenotypes):
    search = search.split(",")
    phenotypes = phenotypes.split(",")
    se = set()
    phe = set()
    for s in search:
        se.add(s.strip())
    for phenotype in phenotypes:
        phe.add(phenotype.strip())
    return se, phe

def redirect_to_connexion():
    return redirect(reverse('authuser:connection'))
