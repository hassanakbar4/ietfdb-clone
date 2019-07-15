# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-28 13:33


from __future__ import absolute_import, print_function, unicode_literals

from django.db import migrations
from django.db.models import F

def forward(apps, schema_editor):
    Document = apps.get_model('doc','Document')
    Document.objects.exclude(type_id__in=('review','recording')).update(uploaded_filename = F('external_url'))
    Document.objects.exclude(type_id__in=('review','recording')).update(external_url="")

    Document.objects.filter(name='slides-100-edu-sessf-patents-at-ietf-an-overview-of-bcp79bis').update(uploaded_filename='slides-100-edu-sessf-patents-at-ietf-an-overview-of-bcp79bis-00.pdf')

    DocHistory = apps.get_model('doc','DocHistory')
    DocHistory.objects.exclude(type_id__in=('review','recording')).update(uploaded_filename = F('external_url'))
    DocHistory.objects.exclude(type_id__in=('review','recording')).update(external_url="")
    
    DocHistory.objects.filter(uploaded_filename='https://www.ietf.org/proceedings/97/slides/slides-97-edu-sessb-local-version-of-newcomers-training-in-korean-00.pdf').update(uploaded_filename='slides-97-edu-sessb-local-version-of-newcomers-training-in-korean-00.pdf')
    DocHistory.objects.filter(uploaded_filename='http://materials-98-codec-opus-newvectors-00.tar.gz').update(uploaded_filename='materials-98-codec-opus-newvectors-00.tar.gz')
    DocHistory.objects.filter(uploaded_filename='http://materials-98-codec-opus-update-00.patch').update(uploaded_filename='materials-98-codec-opus-update-00.patch')
    DocHistory.objects.filter(uploaded_filename='http://slides-100-edu-sessf-patents-at-ietf-an-overview-of-bcp79bis-00.pdf').update(uploaded_filename='slides-100-edu-sessf-patents-at-ietf-an-overview-of-bcp79bis-00.pdf')
    DocHistory.objects.filter(uploaded_filename='http://bluesheets-97-6man-201611150930-00.pdf/').update(uploaded_filename='bluesheets-97-6man-201611150930-00.pdf')
    DocHistory.objects.filter(uploaded_filename='http://agenda-interim-2017-stir-01-stir-01-01.txt').update(uploaded_filename='agenda-interim-2017-stir-01-stir-01-01.txt')
    DocHistory.objects.filter(uploaded_filename='http://agenda-interim-2017-icnrg-02-icnrg-01-05.html').update(uploaded_filename='agenda-interim-2017-icnrg-02-icnrg-01-05.html')


def reverse(apps, schema_editor):
    Document = apps.get_model('doc','Document')
    Document.objects.exclude(type_id__in=('review','recording')).update(external_url = F('uploaded_filename'))
    Document.objects.exclude(type_id__in=('review','recording')).update(uploaded_filename="")

    DocHistory = apps.get_model('doc','DocHistory')
    DocHistory.objects.exclude(type_id__in=('review','recording')).update(external_url = F('uploaded_filename'))
    DocHistory.objects.exclude(type_id__in=('review','recording')).update(uploaded_filename="")


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0008_add_uploaded_filename'),
        ('review', '0008_remove_reviewrequest_old_id'),
        ('meeting', '0011_auto_20190114_0550'),
    ]

    operations = [
        migrations.RunPython(forward,reverse),
    ]
