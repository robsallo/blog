#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas/', 
        views.EntryListView.as_view(),
        name='entry-lista',
    ),
    path(
        # ha sido cambiado a slug  del model en vez de: 'entrada/<pk>/', 
        'entrada/<slug>',
        views.EntryDetailView.as_view(),
        name='entry-detail',
    ),  
]