# Generated by Django 4.2.2 on 2023-06-29 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblia', '0006_livro_ordem'),
    ]

    operations = [
        migrations.AddField(
            model_name='listadeleitura',
            name='plano_de_leitura',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biblia.planodeleitura'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listadeleitura',
            name='capitulo_final',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='listadeleitura',
            name='capitulo_inicial',
            field=models.IntegerField(default=1),
        ),
    ]
