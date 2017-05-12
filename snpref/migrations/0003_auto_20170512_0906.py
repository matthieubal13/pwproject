# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snpref', '0002_auto_20170512_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snp2ref2phen',
            name='phenotype',
        ),
        migrations.RemoveField(
            model_name='snp2ref2phen',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='snp2ref2phen',
            name='snp',
        ),
        migrations.AddField(
            model_name='snp',
            name='phenotype',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='snpref.Phenotype'),
        ),
        migrations.AddField(
            model_name='snp',
            name='ref',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='snp',
            name='rs_id',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Reference',
        ),
        migrations.DeleteModel(
            name='SNP2Ref2Phen',
        ),
    ]
