# Generated by Django 2.2.2 on 2019-06-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=1500)),
                ('image', models.ImageField(upload_to='Home-articles', verbose_name='Imagen')),
                ('typeClass', models.CharField(max_length=40)),
            ],
        ),
    ]
