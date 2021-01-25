from django.db import models
from model_utils.models import TimeStampedModel


class TipoPersona(TimeStampedModel):
    class Meta:
        verbose_name = "Tipo Persona"
        verbose_name_plural = "Tipo Persona"

    nombre = models.CharField('Nombre', max_length=100)

    def __str__(self):
        return str(self.nombre)


class Personas(TimeStampedModel):

    username = models.CharField(
        'Username', max_length=50, unique=True, null=True)
    nombre = models.CharField('Nombre', max_length=100)
    email = models.CharField('Email', max_length=100, blank=True)
    clave = models.CharField(
        'Clave', max_length=6, blank=True)
    telefono = models.IntegerField("Telefono", blank=True, null=True)
    TipoPersona = models.ManyToManyField(
        TipoPersona,
        related_name="Tipo_persona",
    )

    def __str__(self):
        return str(self.nombre) + " " + str(self.telefono)
