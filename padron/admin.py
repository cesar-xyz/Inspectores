from django.contrib import admin

from .models import Padron


@admin.register(Padron)
class PadronAdmin(admin.ModelAdmin):
    list_display = ('nombre_inspector', 'dependencia', 'unidad_administrativa',)
    search_fields = ('nombre_inspector',)
