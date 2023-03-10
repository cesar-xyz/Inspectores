# Importar las clases necesarias de los módulos de Django
from django.db import models
from django.utils.translation import gettext as _

from administrativo.models import Unidad_Administrativa, Autoridad
from .helpers import set_fotografia_path


class Padron(models.Model):
    dependencia = models.ForeignKey(Unidad_Administrativa, blank=False, on_delete=models.CASCADE, related_name='+')
    unidad_administrativa = models.ForeignKey(Unidad_Administrativa, blank=False, on_delete=models.CASCADE,
                                              related_name='+')
    nombre_inspector = models.CharField("nombre del inspector", max_length=128, unique=True, null=False)
    cargo = models.CharField("cargo", max_length=128, unique=True, null=False)
    encargado = models.ForeignKey(Autoridad, blank=False, on_delete=models.CASCADE)
    horario = models.CharField("horario", max_length=128, unique=True, null=False)
    fotografia = models.ImageField(null=True, blank=True, upload_to=set_fotografia_path)
    vigencia = models.DateField(null=True, blank=True)
    materia_giro = models.TextField("materia y giro", max_length=255, unique=True, null=False)
    fundamento_juridico = models.TextField("fundamento juridico", max_length=255, unique=True, null=False)
    domicilio = models.CharField("domicilio", max_length=128, unique=True, null=False)
    telefono = models.CharField("telefono", max_length=128, unique=True, null=False)
    mail = models.CharField("telefono", max_length=128, unique=True, null=False)

    class Meta:
        verbose_name = _("padron")
        verbose_name_plural = _("padron")

    def __str__(self):
        return self.nombre_inspector
