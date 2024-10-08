# Generated by Django 5.0.6 on 2024-06-23 22:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_gallery_alter_social_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('comment', models.CharField(max_length=100, verbose_name='comentario')),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('likes', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='likes')),
            ],
            options={
                'verbose_name': 'Comentario sobre el Blog',
                'verbose_name_plural': 'Comentarios sobre el Blog',
            },
        ),
    ]
