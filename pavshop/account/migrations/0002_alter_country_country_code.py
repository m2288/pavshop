# Generated by Django 4.2.2 on 2023-08-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]