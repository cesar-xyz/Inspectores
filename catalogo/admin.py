from django.contrib import admin

from .models import Catalogo


@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('objeto', 'dependencia', 'unidad_administrativa',)
    search_fields = ('objeto',)
