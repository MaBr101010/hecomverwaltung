from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from schluesselverwaltung.models import Mitarbeiter
from django.shortcuts import render_to_response

def index(request):
    return HttpResponse("Hello World")

class HelloTemplate(TemplateView):

    template_name = 'hello.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Malte'
        return context

def mitarbeiter_all(request):
    return render_to_response('mitarbeiter_all.html',
                              {'ma': Mitarbeiter.objects.all()})

def mitarbeiter(request, persoNr = 1):
    return render_to_response('mitarbeiter.html',
                            {'ma': Mitarbeiter.objects.get(personalnummer = persoNr), })
                             #'schluessel' : Schluessel.objects.get(besitzer_id = persoNr)})