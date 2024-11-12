import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView,
)
#apps entrada models
from applications.entrada.models import Entry
# models home (propio de su app)
from .models import Home

# no es necesrio dado que el models Entry tiene el objects relacionado a su managers.py
##from applications.entrada.managers import EntryManager

# forms
from .forms import SuscribersForm, ContactForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # cargamos el home parte nosotros
        context["home"] = Home.objects.latest('created')
        # contexto de portada
        context["portada"] = Entry.objects.entrada_en_portada()
        # contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entradas_en_home()
        # contexto para entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        # enviamos formulario de suscripcion
        context["form_suscribe"]= SuscribersForm
        return context
    

class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    # recarga la página anterior
    success_url = '.'

# usando un form creado manualmente en el HTML (en este caso en el footer)
class ContactCreateView(CreateView):
    form_class = ContactForm
    # recarga la página anterior
    success_url = '.'





