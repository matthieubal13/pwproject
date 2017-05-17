# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import csv

# Create your views here.
from .models import Phenotype, SNP, Reference, SNPRefPhen
from django.core.urlresolvers import reverse
from .forms import SearchForm

# Creation of functions which search data in Database and return the datas to
# the templates


def phenotype_list(request):
    """View list of all the phenotypes"""
    # Security of the page
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    # List of phenotpes
    phenotypes = Phenotype.objects.all()
    # Count the number of phenotypes
    for phenotype in phenotypes:
        phenotype.snp_number = len(SNPRefPhen.objects.filter(phenotype = phenotype))
    return render(request, 'snpref/phenotype_list.html',
    {'phenotypes': phenotypes})


def phenotype_detail(request, pk):
    """View list of SNPs which depend of a phenotype"""
    # Security of the page
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    # Recover the ID of the phenotype
    phenotype = Phenotype.objects.get(pk = pk)
    # filter the SNPs by the ID of the phenotypes
    snp_refs = SNPRefPhen.objects.filter(phenotype = phenotype)
    return render(request, 'snpref/phenotype_detail.html',
    {'snp_refs' : snp_refs, 'phenotype' : phenotype})


def snp_list(request):
    """View list of all the SNPs"""
    # Security of the page
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    # List of SNPs
    snps = SNP.objects.all()
    for snp in snps:
        snp.ref = SNPRefPhen.objects.filter(snp = snp)
    return render(request, 'snpref/snp_list.html',
    {'snps': snps})


def snp_detail(request, pk):
    """View list of phenotypes which depend of a SNP"""
    # Security of the page
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    # Recover the ID of the SNP
    snp = SNP.objects.get(pk = pk)
    # filter the phenotypes by the ID of the SNPs
    snp_refs = SNPRefPhen.objects.filter(snp = snp)
    return render(request, 'snpref/snp_detail.html',
    {'snp_refs' : snp_refs, 'snp' : snp})


def snp_search(request):
    """View designed to make searching request through database"""
    # Security of the page
    if not request.user.is_authenticated:
        return redirect_to_connexion()
    # test the validity of the search
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            # Retrieve search form.
            search = form.cleaned_data["search"]
            search_phen = form.cleaned_data["phenotypes"]
            # If this field is empty then retrieve all phenotypes.
            if not search_phen:
                phenotypes = Phenotype.objects.all()
            # Else phenotypes are added if they are correct.
            else:
                # Two sets are created to contain good and bad phenotypes.
                phenotypes = set()
                phenotypes_error = set()
                search_phen = search_phen.split(",")
                # For each phenotype typed, a search is performed
                for sp in search_phen:
                    sp = sp.strip(" ").capitalize()
                    phenotype = Phenotype.objects.filter(trait = sp)
                    # If the phenotype is correct it is added.
                    if phenotype:
                        phenotype = phenotype[0]
                        phenotypes.add(phenotype)
                    # If the phenotype is not correct it is put in error.
                    else:
                        phenotypes_error.add(sp)
            # If this field is empty then retrieve all SNPs.
            if not search:
                snps_all = SNP.objects.all()
                snps = set()
                # For each SNP test if the phenotype is in the list.
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
            # Else SNPs are added if they are correct.
            else:
                snps = set()
                search = search.split(",")
                # For each SNP typed, a search is performed
                for s in search:
                    s = s.strip(" ")
                    snp = SNP.objects.filter(rs_id = s)
                    if snp:
                        allowed = False
                        snp = snp[0]
                        snp_ref = SNPRefPhen.objects.filter(snp = snp)
                        if not snp_ref:
                            continue
                        # For each SNP test if the phenotype is in the list.
                        for phenotype in phenotypes:
                            if phenotype.trait == snp_ref[0].phenotype.trait:
                                allowed = True
                                snp.ref = snp_ref[0].ref
                        if allowed:
                            snps.add(snp)
    else:
        form = SearchForm()
    return render(request, 'snpref/search.html', locals())

# Redirects to the connection view
def redirect_to_connexion():
    return redirect(reverse('authuser:connection'))
