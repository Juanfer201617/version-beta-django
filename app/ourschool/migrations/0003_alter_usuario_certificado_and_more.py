# Generated by Django 4.2.7 on 2023-11-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourschool', '0002_alter_usuario_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='certificado',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numero_documento',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_documento',
            field=models.IntegerField(default=0),
        ),
    ]
