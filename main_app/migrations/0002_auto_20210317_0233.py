# Generated by Django 3.1.7 on 2021-03-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='brand',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='product_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
