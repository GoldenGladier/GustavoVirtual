# Generated by Django 2.2.2 on 2019-07-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_page', '0006_recursosdestacados'),
    ]

    operations = [
        migrations.AddField(
            model_name='carreras',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/Careers-articles', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='carreras',
            name='studyPlan',
            field=models.FileField(blank=True, null=True, upload_to='documents/Careers-docs', verbose_name='Study Plan'),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/Home-articles', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='home',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recursosdestacados',
            name='resource',
            field=models.FileField(upload_to='documents/Resource-Relevant', verbose_name='Recurso'),
        ),
    ]
