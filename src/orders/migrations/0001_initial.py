# Generated by Django 2.0.4 on 2018-12-14 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('refunded', 'Refunded'), ('shipped', 'Shipped')], default='created', max_length=120)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=50, max_digits=50)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('cart', models.ForeignKey(on_delete='cascade', to='carts.Cart')),
            ],
        ),
    ]