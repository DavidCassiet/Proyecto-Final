from django.contrib import admin
from .models import Pregunta, Respuesta

# Register your models here.

class RespuestaInLine(admin.TabularInline):
    model = Respuesta

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInLine]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)