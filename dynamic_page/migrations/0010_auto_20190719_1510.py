# Generated by Django 2.2.2 on 2019-07-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_page', '0009_auto_20190719_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
