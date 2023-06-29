from django.contrib import admin

from biblia.models import Livro, PlanoDeLeitura, ListaDeLeitura


class LivroAdmin(admin.ModelAdmin):
    model = Livro
    list_display = ['ordem', 'nome', 'quantidade_capitulos']


admin.site.register(Livro, LivroAdmin)


class PlanoDeLeituraAdmin(admin.ModelAdmin):
    model = PlanoDeLeitura
    list_display = ['nome', 'data_inicio', 'data_fim', 'ativo', 'quandidade_capitulos_por_dia']


admin.site.register(PlanoDeLeitura, PlanoDeLeituraAdmin)


class ListaDeLeituraAdmin(admin.ModelAdmin):
    model = ListaDeLeitura
    list_display = ['data', 'livro', 'capitulo_inicial', 'capitulo_final', 'plano_de_leitura']
    ordering = ['id', 'data']
    list_filter = ['plano_de_leitura__nome']


admin.site.register(ListaDeLeitura, ListaDeLeituraAdmin)
