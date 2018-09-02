# Generated by Django 2.0.4 on 2018-09-02 10:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstAid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Item name')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Item picture')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short description')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
