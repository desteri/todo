# Generated by Django 3.1.3 on 2021-01-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210119_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshop',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]