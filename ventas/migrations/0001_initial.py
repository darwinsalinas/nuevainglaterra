# Generated by Django 2.2.6 on 2019-10-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=250)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Comunidad')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.EstadoCivil')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Genero')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150)),
                ('apellidos', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=250)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Comunidad')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Genero')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('numero_factura', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Cliente')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogos.TipoVenta')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Vendedor')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Articulo')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Venta')),
            ],
            options={
                'verbose_name': 'Detalle de venta',
                'verbose_name_plural': 'Detalles de ventas',
            },
        ),
    ]
