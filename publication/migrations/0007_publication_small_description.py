# Generated by Django 5.0.6 on 2024-06-24 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0006_publication_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='small_description',
            field=models.CharField(default=1, max_length=100, verbose_name='Nombre'),
            preserve_default=False,
        ),
    ]
