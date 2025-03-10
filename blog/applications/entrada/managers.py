from django.db import models

class EntryManager(models.Manager):
    """ procedimiento para entrada """

    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created').first()
    
    def entradas_en_home(self):
        # devuelve las primeras 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('created')[:4]
    
    def entradas_recientes(self):
        # devuelve las ultimas 3 entradas recientes
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:3]
    
    def buscar_entrada(self, kword, categoria):
        # procedimiento para buscar entradas por categoria o palabra clave
        if len(categoria) > 0:
            return self.filter(
                category__short_name = categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')

            

