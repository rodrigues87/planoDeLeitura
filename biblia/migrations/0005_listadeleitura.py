# Generated by Django 4.2.2 on 2023-06-29 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblia', '0004_planodeleitura_quandidade_capitulos_por_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaDeLeitura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('capitulo_inicial', models.IntegerField()),
                ('capitulo_final', models.IntegerField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblia.livro')),
            ],
        ),
    ]
