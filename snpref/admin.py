# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Phenotype, SNP

admin.site.register(Phenotype)
admin.site.register(SNP)

# Register your models here.
