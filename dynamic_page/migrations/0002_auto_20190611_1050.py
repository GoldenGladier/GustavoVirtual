# Generated by Django 2.2.2 on 2019-06-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(upload_to='dynamic_page/assets/img/Home-articles', verbose_name='Imagen'),
        ),
    ]
