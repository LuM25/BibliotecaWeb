# Generated by Django 4.0.5 on 2022-07-02 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
            ],
        ),
    ]