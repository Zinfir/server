# Generated by Django 2.1.1 on 2019-01-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
