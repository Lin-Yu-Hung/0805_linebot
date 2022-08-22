# Generated by Django 4.0.5 on 2022-08-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linebotApp', '0008_company_lineid'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_hunting',
            name='job_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='job_hunting',
            name='job_title2',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='job_hunting',
            name='job_type',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='maxSalary',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='minSalary',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='job_hunting',
            name='maxSalary',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='job_hunting',
            name='minSalary',
            field=models.IntegerField(default=''),
        ),
    ]