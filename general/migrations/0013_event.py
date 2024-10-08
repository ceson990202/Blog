# Generated by Django 5.0.6 on 2024-07-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_alter_blogcomment_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='events', verbose_name='Imagen')),
                ('active', models.BooleanField(default=False, verbose_name='activo')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
