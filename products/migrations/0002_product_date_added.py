# Generated by Django 3.2.15 on 2022-08-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateField(blank=True, null=True),
        ),
    ]
