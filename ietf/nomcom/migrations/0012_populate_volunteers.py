# Copyright The IETF Trust 2021 All Rights Reserved
# Generated by Django 2.2.24 on 2021-06-10 12:50

from django.db import migrations

def forward(apps, schema_editor):
    NomCom = apps.get_model('nomcom','NomCom')
    nc = NomCom.objects.filter(group__acronym='nomcom2021').first()
    if nc is None:
        return  # nothing to do if the NomCom in question does not exist

    nc.is_accepting_volunteers = True
    nc.save()
    
    volunteers = [
        (21684, 'Futurewei Technologies'), # Barry Leiba
        (117988, 'Google LLC'), # Benjamin M. Schwartz
        (122671, 'Fastmail Pty Ltd'), # Bron Gondwana
        (124329, 'Huawei'), # Cheng Li
        (113580, 'China Mobile'), # Weiqiang Cheng
        (22933, 'LabN Consulting'), # Christian Hopps
        (102391, 'Futurewei Technologies, Inc'), # Donald E. Eastlake 3rd
        (111477, 'Huawei'), # Dhruv Dhody
        (12695, 'Mozilla'), # Eric Rescorla
        (17141, 'APNIC'), # George G. Michaelson
        (108833, 'Huawei'), # Luigi Iannone
        (118908, 'Huawei Technologies'), # Giuseppe Fioccola
        (5376, 'Vigil Security, LLC'), # Russ Housley
        (118100, 'Equinix'), # Ignas Bagdonas
        (107287, 'rtfm llp'), # Jim Reid
        (123344, 'Netflix'), # Theresa Enghardt
        (109226, 'Huawei'), # Italo Busi
        (113152, 'Ericsson'), # Jaime Jimenez
        (111354, 'Juniper Networks'), # John Drake
        (112342, 'Cisco Systems, Inc.'), # Jakob Heitz
        (109207, 'Huawei Technologies Co., Ltd.'), # 江元龙
        (110737, 'Huawei Technologies'), # Jie Dong
        (109330, 'Ericsson'), # John Preuß Mattsson
        (123589, 'Nokia'), # Julien Maisonneuve
        (124655, 'UK National Cyber Security Centre (NCSC)'), # Kirsty Paine
        (119463, 'Akamai Technologies, Inc.'), # Kyle Rose
        (109983, 'Huawei Technologies Co.,Ltd.'), # Bo Wu
        (2097, 'Cisco Systems'), # Eliot Lear
        (567, 'UCLA'), # Lixia Zhang
        (107762, 'Huawei'), # Mach Chen
        (125198, 'Juniper Networks'), # Melchior Aelmans
        (104294, 'Ericsson'), # Magnus Westerlund
        (104495, 'Impedance Mismatch LLC'), # Marc Petit-Huguenin
        (119947, 'Painless Security, LLC'), # Margaret Cullen
        (102830, 'Independent'), # Mary Barnes
        (116593, 'Fastly'), # Patrick McManus
        (102254, 'Sandelman Software Works'), # Michael Richardson
        (20356, 'Apple'), # Ted Lemon
        (103881, 'Fastly'), # Mark Nottingham
        (106741, 'NthPermutation Security'), # Michael StJohns
        (116323, 'Moulay Ismail University of Meknes, Morocco'), # Nabil Benamar
        (20106, 'W3C/MIT'), # Samuel Weiler
        (105691, 'cisco'), # Ole Trøan
        (121160, 'Independent, Amazon'), # Padma Pillay-Esnault
        (115824, 'Cisco Systems'), # Pascal Thubert
        (122637, 'Huawei Technologies Co.,Ltd.'), # Shuping Peng
        (112952, 'Huawei'), # Haibo Wang
        (5234, 'IIJ Research Lab & Arrcus Inc'), # Randy Bush
        (101568, 'Juniper Networks'), # Ron Bonica
        (123443, 'Huawei Technologies Co.,Ltd.'), # Bing Liu (Remy)
        (18321, 'Episteme Technology Consulting LLC'), # Pete Resnick
        (18427, 'Akamai'), # Rich Salz
        (126259, 'Huawei Technologies Co.,Ltd.'), # Fan Yang
        (115724, 'Juniper Networks'), # Shraddha Hegde
        (125509, 'Tencent'), # Shuai Zhao
        (110614, 'Huawei'), # Tal Mizrahi
        (123395, 'APNIC'), # Tom Harrison
        (116516, 'Juniper Networks'), # Tarek Saad
        (11834, 'Futurewei USA'), # Toerless Eckert
        (123962, 'Open-Xchange'), # Vittorio Bertola
        (126530, 'Huawei'), # Yali Wang
        (106199, 'Ericsson'), # Wassim Haddad
        (125173, 'Huawei'), # Wei Pan
        (111299, 'ZTE Corporation'), # Xiao Min
        (113285, 'Huawei Technologies'), # XiPeng Xiao
        (116337, 'Futurewei Technologies Inc.'), # Yingzhen Qu
        (123974, 'ZTE'), # Zheng Zhang
        (117500, 'Huawei'), # Guangying Zheng
        (115934, 'Huawei Technologies'), # Haomian Zheng
        (110966, 'Juniper'), # Zhaohui (Jeffrey) Zhang
    ]

    for pk, affiliation in volunteers:
        nc.volunteer_set.create(person_id=pk, affiliation=affiliation)

def reverse(apps, schema_editor):
    Volunteer = apps.get_model('nomcom','Volunteer')
    Volunteer.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('nomcom', '0011_volunteers'),
    ]

    operations = [
        migrations.RunPython(forward,reverse)
    ]
