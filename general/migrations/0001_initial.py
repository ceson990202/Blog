# Generated by Django 5.0.6 on 2024-06-23 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Titulo')),
                ('small_description', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Presentacion',
                'verbose_name_plural': 'Presentacion',
            },
        ),
    ]
