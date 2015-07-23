# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lager',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('raum', models.CharField(max_length=50, verbose_name='Raum')),
                ('schrank', models.CharField(max_length=20, verbose_name='Schrank')),
            ],
        ),
        migrations.CreateModel(
            name='Mitarbeiter',
            fields=[
                ('vorname', models.CharField(max_length=30, verbose_name='Vorname')),
                ('nachname', models.CharField(max_length=30, verbose_name='Nachname')),
                ('personalnummer', models.IntegerField(primary_key=True, serialize=False, verbose_name='Personalnummer')),
                ('activ', models.BooleanField()),
                ('gruppe', models.CharField(choices=[('AZ', 'Auszubildender'), ('IT', 'IT-Abteilung'), ('TK', 'TK-Abteilung'), ('SW', 'Software-Abteilung'), ('VT', 'Vertriebs-Abteilung'), ('LT', 'Fuehrungskraft'), ('GFN', 'GFN- Umschuler')], max_length=7, default=False, verbose_name='Abteilung')),
            ],
        ),
        migrations.CreateModel(
            name='Schliessgruppe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Schluessel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('schluesselnummer', models.CharField(max_length=8, verbose_name='Schluesselnummer')),
                ('hersteller', models.CharField(max_length=20, default=False, verbose_name='Hersteller')),
                ('uebergabe_datum', models.DateTimeField()),
                ('besitzer', models.ForeignKey(default=False, to='schluesselverwaltung.Mitarbeiter', verbose_name='Besitzer')),
                ('schliessgruppe', models.ForeignKey(to='schluesselverwaltung.Schliessgruppe')),
            ],
        ),
        migrations.CreateModel(
            name='Tuer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('seriennummer', models.CharField(max_length=30, verbose_name='Seriennummer')),
                ('ort', models.CharField(max_length=50, verbose_name='Ort')),
                ('kennziffer', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='schliessgruppe',
            name='tuer',
            field=models.ManyToManyField(to='schluesselverwaltung.Tuer'),
        ),
    ]
