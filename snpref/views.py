# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
<<<<<<< HEAD
from .models import Phenotype
from .models import SNP
=======
>>>>>>> df6522d86bbdd6ef5fd7cfd03e01051d856ed95a

# Create your views here.
from .models import Phenotype

def phenotype_list(request):
    phenotypes = Phenotype.objects.all()
    return render(request, 'snpref/phenotype_list.html',
    {'phenotypes': phenotypes})

def snp_list(request):
    snp = SNP.objects.all()
    return render(request, 'snpref/snp_list.html',
    {'snp': snp})
