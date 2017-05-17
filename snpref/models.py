# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Phenotype(models.Model):
    """Represents phenotypes with a trait."""
    trait = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.trait)


class SNP(models.Model):
    """Represents SNP with an ID."""
    rs_id = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.rs_id)


class Reference(models.Model):
    """Represents a reference which is simply a URL"""
    url = models.URLField()

    def __str__(self):
        return str(self.url)


class SNPRefPhen(models.Model):
    """Represents the association between a phenotype, a SNP and a reference."""
    phenotype = models.ForeignKey(Phenotype, on_delete = models.CASCADE)
    snp = models.ForeignKey(SNP, on_delete = models.CASCADE)
    ref = models.ForeignKey(Reference, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.phenotype) + " - " + str(self.snp)
