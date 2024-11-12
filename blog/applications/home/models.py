from django.db import models

# apps terceros (se instaló con pip install django-model-utils)
# no requiere para esta apps que se declare en base.py
# esto permitirá manejar fechas de creación y modificación de registros en este models
from model_utils.models import TimeStampedModel

# Create your models here.

class Home(TimeStampedModel):
    """ Models para datos de la pantalla Home """

    title = models.CharField(
        'Nombre', 
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros', 
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono contacto', 
        max_length=20
    )
    
    # fecha crweación y modificación se obtienen de la app instalada
    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal (home)'
    
    def __str__(self):
        return self.title

class Suscribers(TimeStampedModel):
    """ Suscripciones """

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores (suscribers)'

    def __str__(self):
        return self.email
    
class Contact(TimeStampedModel):
    """ Formulario de contacto """
    
    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.EmailField()
    messagge = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes (contact)'

    def __str__(self):
        return self.full_name