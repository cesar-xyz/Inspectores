# Importar las clases necesarias de los módulos de Django
from django.db import models
from django.utils.translation import gettext as _

class Unidad_Administrativa(models.Model):
    nombre = models.CharField("nombre", max_length=128, unique=True, null=False)
    unidad_administrativa = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="+")

    class Meta:
        verbose_name = _("unidad administrativa")
        verbose_name_plural = _("unidades administrativas")

    def __str__(self):
        return self.nombre


class Autoridad(models.Model):
    nombre = models.CharField("nombre", max_length=128, unique=True, null=False)
    cargo = models.CharField("cargo", max_length=128, unique=True, null=False)
    telefono = models.CharField("telefono", max_length=128, unique=True, null=False)
    mail = models.CharField("mail", max_length=128, unique=True, null=False)

    class Meta:
        verbose_name = _("autoridad")
        verbose_name_plural = _("autoridad")

    def __str__(self):
        return self.nombre
