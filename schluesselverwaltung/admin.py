from django.contrib import admin
from schluesselverwaltung.models import *

admin.site.register(Mitarbeiter)
admin.site.register(Schliessgruppe)
admin.site.register(Schluessel)
admin.site.register(Lager)
admin.site.register(Tuer)
