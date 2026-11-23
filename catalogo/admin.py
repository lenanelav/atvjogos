from django.contrib import admin
from .models import Desenvolvedora, Plataforma, Jogo


@admin.register(Desenvolvedora)
class DesenvolvedoraAdmin(admin.ModelAdmin):
    search_fields = ['nome']


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    search_fields = ['nome']


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ano_lancamento', 'desenvolvedora', 'plataforma']
    list_filter = ['desenvolvedora', 'plataforma']
    search_fields = ['nome']