# Generated by Django 4.2.1 on 2023-05-29 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locadora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locacao',
            name='filme',
            field=models.ManyToManyField(to='locadora.filme'),
        ),
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.categoria'),
        ),
        migrations.AlterField(
            model_name='locacao',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.cliente'),
        ),
    ]
