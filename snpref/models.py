# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Phenotype(models.Model):
    trait = models.CharField(max_length = 100)

    def __str__(self):
        return str(self.trait)


class SNP(models.Model):
    rs_id = models.CharField(max_length = 20)
    phenotype = models.ForeignKey(Phenotype, on_delete = models.CASCADE,
    default = None)
    ref = models.URLField(default = None)

    def __str__(self):
        return str(self.rs_id) + " - " + str(self.phenotype)
