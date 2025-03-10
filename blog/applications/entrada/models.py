# standard library python
from datetime import timedelta, datetime
# djnago library
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# app terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# managers
from .managers import EntryManager

# Create your models here.

class Category(TimeStampedModel):
    """ Categoria de una entrada """

    short_name = models.CharField(
        'Nombre corto', 
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Nombre', 
        max_length=30
    )

    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias (category)'

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    """ etiquetas de una articulo """

    name = models.CharField(
        'Nombre', 
        max_length=50
    )

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags (tag)'

    def __str__(self):
        return self.name

class Entry(TimeStampedModel):
    """ modelo para entrada o articulos """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen', 
        upload_to='Entry'
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(
        editable=False,
        max_length=300
    )

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas (entry)'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # calcular total segundos hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds= int(total_time.total_seconds())
         # genera slug para que aparezca en la url respectiva
        slug_unique= '%s %s' % (self.title, str(seconds))
        self.slug = slugify(slug_unique)
        super(Entry, self).save(*args, **kwargs)
        





        
        

