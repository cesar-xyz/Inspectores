# Importar las clases necesarias de los módulos de Django
from django.db import models
from django.utils.translation import gettext as _

from administrativo.models import Unidad_Administrativa, Autoridad


class Catalogo(models.Model):
    dependencia = models.ForeignKey(Unidad_Administrativa, blank=False, on_delete=models.CASCADE, related_name='+')
    unidad_administrativa = models.ForeignKey(Unidad_Administrativa, blank=False, on_delete=models.CASCADE,
                                              related_name='+')
    OPCIONES_VERIFICACION = (
        ('Inspección', 'Inspección'),
        ('Verificación', 'Verificación'),
    )
    tipo = models.CharField("tipo", max_length=12, choices=OPCIONES_VERIFICACION)

    objeto = models.TextField("objeto", max_length=255, unique=True, null=False)
    actividad_servicio = models.TextField("actividad o servicio", max_length=255, unique=True, null=False)
    disposicion_fundamento = models.TextField("disposición y fundamentos", max_length=255, unique=True, null=False)
    info_organo = models.TextField("información órgano", max_length=255, unique=True, null=False)
    encargado = models.ForeignKey(Autoridad, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("catalogo")
        verbose_name_plural = _("catalogos")

    def __str__(self):
        return self.actividad_servicio

