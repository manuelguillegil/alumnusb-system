# Generated by Django 3.0.3 on 2020-03-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20200317_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='Picture',
            field=models.ImageField(default='static/achiev_img/C.png', upload_to='static/achiev_img/'),
        ),
    ]
