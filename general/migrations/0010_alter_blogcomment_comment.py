# Generated by Django 5.0.6 on 2024-07-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_alter_blogcomment_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(max_length=250, verbose_name='comentario'),
        ),
    ]
