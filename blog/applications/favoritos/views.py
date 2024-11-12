from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    View,
    DeleteView,
)
from .models import Favorites
from applications.entrada.models import Entry

# Create your views here.

class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url= reverse_lazy('users_app:user-login')

    def get_queryset(self) -> QuerySet[Any]:
        return Favorites.objects.entradas_user(self.request.user)
    
class AddFavoritosView(LoginRequiredMixin, View):

    login_url= reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        # recuperar el usuario
        usuario= self.request.user
        entrada=Entry.objects.get(id=self.kwargs['pk'])
        # registramos favorito
        Favorites.objects.create(
            user=usuario,
            entry=entrada,
        )

        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil'
            )
        )


class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')
    




