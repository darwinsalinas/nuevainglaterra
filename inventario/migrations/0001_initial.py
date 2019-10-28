# Generated by Django 2.2.6 on 2019-10-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('codigo', models.CharField(max_length=20)),
                ('serie', models.CharField(max_length=100)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Modelo')),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Presentacion')),
                ('tipo_articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.TipoArticulo')),
                ('unidad_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.UnidadMedida')),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
            },
        ),
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Tipo de movimiento',
                'verbose_name_plural': 'Tipos de movimientos',
            },
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('referencia', models.CharField(max_length=200)),
                ('cantidad', models.FloatField()),
                ('valor_unitario', models.FloatField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Articulo')),
                ('tipo_movimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.TipoMovimiento')),
            ],
            options={
                'verbose_name': 'Kárdex',
                'verbose_name_plural': 'Kárdex',
            },
        ),
    ]