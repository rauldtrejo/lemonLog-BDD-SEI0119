# Generated by Django 3.1.7 on 2021-03-18 03:00

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_article_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
        ),
    ]