# Generated by Django 3.0.3 on 2020-02-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200225_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumncsv',
            name='Account_id',
            field=models.CharField(default='0000000', max_length=50),
        ),
    ]
