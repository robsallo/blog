from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel
# Create your models here.

from applications.entrada.models import Entry 
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    """  Modelo para Favoritos """

    user= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,        
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE

    )

    objects = FavoritesManager()

    # permite que guarde una sola vez la relación en favorites
    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas (favorites)'

    def __str__(self):
        return self.entry.title

