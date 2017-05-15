# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Phenotype, SNP, Reference, SNPRefPhen

admin.site.register(Phenotype)
admin.site.register(SNP)
admin.site.register(Reference)
admin.site.register(SNPRefPhen)

# Register your models here.
