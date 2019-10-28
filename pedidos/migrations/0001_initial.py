# Generated by Django 2.2.6 on 2019-10-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ventas', '0001_initial'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrigenPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Origen de venta',
                'verbose_name_plural': 'Orígenes de ventas',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Cliente')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pedidos.OrigenPedido')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ventas.Vendedor')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('precio_venta', models.FloatField()),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Articulo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido')),
            ],
            options={
                'verbose_name': 'Detalle de pedido',
                'verbose_name_plural': 'Detalles de pedidos',
            },
        ),
    ]