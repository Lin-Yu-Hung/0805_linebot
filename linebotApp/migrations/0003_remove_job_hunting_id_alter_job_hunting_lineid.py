# Generated by Django 4.0.5 on 2022-08-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linebotApp', '0002_job_hunting_lineid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_hunting',
            name='id',
        ),
        migrations.AlterField(
            model_name='job_hunting',
            name='lineId',
            field=models.CharField(default='', max_length=255, primary_key=True, serialize=False),
        ),
    ]