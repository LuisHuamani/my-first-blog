# Generated by Django 3.1.6 on 2021-02-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carrusel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to='carrusel')),
            ],
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='descripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='empresas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to='empresas')),
            ],
        ),
        migrations.CreateModel(
            name='servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('texto', models.CharField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to='servicios')),
            ],
        ),
    ]