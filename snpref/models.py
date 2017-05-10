# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Phenotype(models.Model):
    trait = models.CharField(max_length = 100)
    ref = models.URLField()

    def __str__(self):
        return self.trait + "\t" + self.ref

class SNP(models.Model):
    phenotype = models.ForeignKey(Phenotype, on_delete = models.CASCADE)
    rs_id = models.CharField(max_length = 15)

    def __str__(self):
        return str(self.phenotype) + "\t" + self.rs_id
