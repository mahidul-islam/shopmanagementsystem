# Generated by Django 2.0.4 on 2018-12-08 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Item name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('available_stock', models.PositiveIntegerField(default=0)),
                ('required_stock', models.PositiveIntegerField(default=1)),
                ('not_in_stock', models.BooleanField(default=True)),
                ('need_to_stock', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='item_pics/%Y-%m-%d/', verbose_name='Item picture')),
                ('description', models.TextField(blank=True, max_length=400, null=True, verbose_name='Short description')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
