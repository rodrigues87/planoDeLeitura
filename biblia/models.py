from math import ceil

from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


class Livro(models.Model):
    ordem = models.IntegerField()
    nome = models.CharField(max_length=50)
    quantidade_capitulos = models.IntegerField()

    def __str__(self):
        return self.nome


class PlanoDeLeitura(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField()
    livros = models.ManyToManyField(Livro, blank=True)
    quandidade_capitulos_por_dia = models.IntegerField()

    def __str__(self):
        return self.nome


class ListaDeLeitura(models.Model):
    data = models.DateField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    capitulo_inicial = models.IntegerField(default=1)
    capitulo_final = models.IntegerField(default=0)
    plano_de_leitura = models.ForeignKey(PlanoDeLeitura, on_delete=models.CASCADE)


@receiver(post_save, sender=PlanoDeLeitura)
def update_stock(sender, instance, **kwargs):
    total_days = abs((instance.data_fim - instance.data_inicio).days)
    total_de_capitulos = 0
    for livro in instance.livros.all():
        total_de_capitulos = total_de_capitulos + livro.quantidade_capitulos

    capitulos_dia = - (-total_de_capitulos // total_days)

    capitulos_exedentes = 0

    data_de_leitura = instance.data_inicio

    for livro in instance.livros.all():
        lista_de_leitura = ListaDeLeitura()

        if capitulos_exedentes != 0:
            ListaDeLeitura.objects.get_or_create(data=data_de_leitura, livro=livro,
                                                 capitulo_inicial=1,
                                                 capitulo_final=capitulos_exedentes, plano_de_leitura=instance)

        lista_de_leitura.capitulo_inicial = lista_de_leitura.capitulo_inicial + capitulos_exedentes

        while lista_de_leitura.capitulo_final < livro.quantidade_capitulos:
            lista_de_leitura.data = data_de_leitura
            lista_de_leitura.livro = livro
            if lista_de_leitura.capitulo_final > 0:
                lista_de_leitura.capitulo_inicial = lista_de_leitura.capitulo_final + 1
            lista_de_leitura.capitulo_final = lista_de_leitura.capitulo_inicial + capitulos_dia

            if lista_de_leitura.capitulo_final > livro.quantidade_capitulos:
                capitulos_exedentes = lista_de_leitura.capitulo_final - livro.quantidade_capitulos
                lista_de_leitura.capitulo_final = livro.quantidade_capitulos
            else:
                data_de_leitura = data_de_leitura + datetime.timedelta(days=1)

            ListaDeLeitura.objects.get_or_create(data=data_de_leitura, livro=livro,
                                                 capitulo_inicial=lista_de_leitura.capitulo_inicial,
                                                 capitulo_final=lista_de_leitura.capitulo_final,
                                                 plano_de_leitura=instance)
