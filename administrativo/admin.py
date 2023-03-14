from django.contrib import admin

from .models import Unidad_Administrativa, Autoridad, Hora_entrada_salida, Horario


@admin.register(Unidad_Administrativa)
class UnidadAdministrativaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Hora_entrada_salida)
class HoraAdmin(admin.ModelAdmin):
    list_display = ('hora_inicio', 'hora_fin')
    search_fields = ('hora_inicio', 'hora_fin')


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


admin.site.register(Horario, HorarioAdmin)
