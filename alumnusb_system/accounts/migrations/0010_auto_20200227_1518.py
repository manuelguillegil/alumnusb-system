# Generated by Django 3.0.3 on 2020-02-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200227_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumncsv',
            name='Account_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Average_gift',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Best_gift_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Best_gift_year_total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Carnet',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Codigo_Alumn_USB',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Cohorte',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Donor',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Email',
            field=models.EmailField(max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='First_gift_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='First_name',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Graduate_campus',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Graduate_degree',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Instagram_account',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Largest_gift',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Last_gift_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Last_name',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mailing_city',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mailing_country',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mailing_state',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Middle_name',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Mobile',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Smallest_gift',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Social_networks',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Total_gifts',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Total_number_of_gifts',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Twitter_account',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='USB_alumn',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='USB_undergrad_campus',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Undergrad_degree',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Work_email',
            field=models.EmailField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='alumncsv',
            name='Workplace',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
