# Generated by Django 2.2.12 on 2021-11-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notas',
            name='Freq_1',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='Frequência 1º Bim'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notas',
            name='Freq_2',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='Frequência 2º Bim'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notas',
            name='Freq_3',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='Frequência 3º Bim'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notas',
            name='Freq_4',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='Frequência 4º Bim'),
            preserve_default=False,
        ),
    ]
