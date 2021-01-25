from django.db import models
from model_utils.models import TimeStampedModel


class Empresa(TimeStampedModel):

    nit = models.CharField('Nit/Identifiacion')
    nombre = models.CharField('Nombre/Razón Social', max_length=100)
    resolucion = models.CharField('Resolución')
    telefono = models.BigIntegerField('Telefono')
    tiempo_espera = models.IntegerField('Tiempo de espera')

    def __str__(self):
        return str(self.nit)+" "+str(self.nombre)
