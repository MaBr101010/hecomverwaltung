from django.db import models

class Mitarbeiter(models.Model):
    vorname = models.CharField('Vorname', max_length=30)
    nachname = models.CharField('Nachname', max_length=30)
    personalnummer = models.IntegerField('Personalnummer', primary_key=True)
    activ = models.BooleanField()
    ABTEILUNG = (
        ('AZ', 'Auszubildender'),
        ('IT', 'IT-Abteilung'),
        ('TK', 'TK-Abteilung'),
        ('SW', 'Software-Abteilung'),
        ('VT', 'Vertriebs-Abteilung'),
        ('LT', 'Fuehrungskraft'),
        ('GFN', 'GFN- Umschuler')
    )
    gruppe = models.CharField('Abteilung',max_length=7, choices=ABTEILUNG, default=False)


    def __str__(self):
       return '%s, %s, %s' % (self.nachname, self.vorname, self.personalnummer)

class Lager(models.Model):
    id = models.IntegerField(primary_key=True)
    raum = models.CharField('Raum', max_length=50)
    schrank = models.CharField('Schrank', max_length=20)

    def __str__(self):
        return '%s, %s' % (self.raum, self.schrank)

class Tuer(models.Model):
    seriennummer = models.CharField('Seriennummer', max_length=30)
    ort = models.CharField('Ort', max_length=50)
    kennziffer = models.CharField(max_length= 20)

    def __str__(self):
        return self.ort

class Schliessgruppe(models.Model):
    name = models.CharField(max_length=30)
    tuer = models.ManyToManyField(Tuer)

    def __str__(self):
        return self.name

class Schluessel(models.Model):
    id = models.IntegerField(primary_key=True)
    besitzer = models.ForeignKey(Mitarbeiter, verbose_name="Besitzer", default=False)
    schluesselnummer = models.CharField('Schluesselnummer', max_length=8)
    hersteller = models.CharField('Hersteller', max_length=20, default=False )
    uebergabe_datum = models.DateTimeField()
    schliessgruppe = models.ForeignKey(Schliessgruppe)

    def __str__(self):
        return '%s, %s' % (self.besitzer, self.schluesselnummer)
