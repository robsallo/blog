# Generated by Django 4.1 on 2024-11-08 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Mensajes (contact)'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Pagina Principal', 'verbose_name_plural': 'Pagina Principal (home)'},
        ),
        migrations.AlterModelOptions(
            name='suscribers',
            options={'verbose_name': 'Suscriptor', 'verbose_name_plural': 'Suscriptores (suscribers)'},
        ),
    ]
