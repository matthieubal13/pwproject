# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Return the name of the phenotype
class Phenotype(models.Model):
    trait = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.trait)


# Return the name of the SNP
class SNP(models.Model):
    rs_id = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.rs_id)

# Return the references of a SNP
class Reference(models.Model):
    url = models.URLField()
    def __str__(self):
        return str(self.url)

# Return primary keys of other tables
class SNPRefPhen(models.Model):
    phenotype = models.ForeignKey(Phenotype, on_delete = models.CASCADE)
    snp = models.ForeignKey(SNP, on_delete = models.CASCADE)
    ref = models.ForeignKey(Reference, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.phenotype) + " - " + str(self.snp)
