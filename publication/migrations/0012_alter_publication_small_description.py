# Generated by Django 5.0.6 on 2024-07-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0011_alter_publicationcomment_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='small_description',
            field=models.TextField(max_length=100, verbose_name='Pequeña descripcion'),
        ),
    ]
