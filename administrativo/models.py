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


class Hora_entrada_salida(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        verbose_name = _("hora entrada y salida")
        verbose_name_plural = _("horas de entrada y salida")

    def __str__(self):
        return f'{self.hora_inicio.strftime("%I:%M %p")} - {self.hora_fin.strftime("%I:%M %p")}'


class Horario(models.Model):
    lunes = models.ForeignKey(Hora_entrada_salida, on_delete=models.CASCADE, related_name='lunes_set', null=True, blank=True)
    martes = models.ForeignKey(Hora_entrada_salida, on_delete=models.CASCADE, related_name='martes_set', null=True, blank=True)
    miercoles = models.ForeignKey(Hora_entrada_salida, on_delete=models.CASCADE, related_name='miercoles_set', null=True,
                                  blank=True)
    jueves = models.ForeignKey(Hora_entrada_salida, on_delete=models.CASCADE, related_name='jueves_set', null=True, blank=True)
    viernes = models.ForeignKey(Hora_entrada_salida, on_delete=models.CASCADE, related_name='viernes_set', null=True, blank=True)
    sabado = models.ForeignKey(Hora_entrada_salida, on_delete=models.CASCADE, related_name='sabado_set', null=True, blank=True)
    domingo = models.ForeignKey(Hora_entrada_salida, on_delete=models.CASCADE, related_name='domingo_set', null=True, blank=True)

    def __str__(self):
        horarios = {}
        for dia in ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']:
            horario_dia = getattr(self, dia)
            if horario_dia:
                horario_str = horario_dia.hora_inicio.strftime('%I:%M %p') + "-" + horario_dia.hora_fin.strftime(
                    '%I:%M %p')
                if horario_str not in horarios:
                    horarios[horario_str] = []
                horarios[horario_str].append(dia.capitalize())

        dias_str = []
        for horario, dias in horarios.items():
            dias_str.append(', '.join(dias) + ' ' + horario)

        return ' '.join(dias_str)
