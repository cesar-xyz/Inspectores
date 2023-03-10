from django.contrib import admin

from .models import Unidad_Administrativa, Autoridad


@admin.register(Unidad_Administrativa)
class UnidadAdministrativaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
