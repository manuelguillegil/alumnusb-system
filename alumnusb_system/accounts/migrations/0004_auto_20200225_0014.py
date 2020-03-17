# Generated by Django 3.0.3 on 2020-02-25 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200224_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_information',
            name='USB_undergrad_campus',
            field=models.CharField(choices=[('Sartenejas', 'SA'), ('Litoral', 'LI')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user_information',
            name='Undergrad_degree',
            field=models.CharField(choices=[('Ingenieria Electrica', 'IE'), ('Ingenieria Mecanica', 'IM'), ('Ingenieria Quimica', 'IQ'), ('Ingenieria Electronica', 'IEl'), ('Ingenieria de Materiales', 'IMa'), ('Ingenieria de la Computacion', 'IC'), ('Ingenieria Geofisica', 'IG'), ('Ingenieria de Produccion', 'IP'), ('Ingenieria de Mantenimiento', 'IMn'), ('Ingenieria de Telecomunicaciones', 'IT'), ('Arquitectura', 'AR'), ('Urbanismo', 'UR'), ('Licenciatura en Quimica', 'LQ'), ('Licenciatura en Matematicas', 'LM'), ('Licenciatura en Fisica', 'LF'), ('Licenciatura en Biologia', 'LB'), ('Licenciatura en Comercio Internacional', 'LCI'), ('Licenciatura en Gestion de la Hospitalidad', 'LGH'), ('Licenciatura en Estudios y Artes Liberales', 'EL'), ('Economia', 'EC'), ('Otro', 'OT')], max_length=42),
        ),
    ]