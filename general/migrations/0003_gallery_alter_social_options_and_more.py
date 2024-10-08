# Generated by Django 5.0.6 on 2024-06-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_social_alter_presentation_small_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galeria',
            },
        ),
        migrations.AlterModelOptions(
            name='social',
            options={'verbose_name': 'Redes sociales', 'verbose_name_plural': 'Redes sociales'},
        ),
        migrations.AlterField(
            model_name='presentation',
            name='small_description',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Titulo'),
        ),
    ]
