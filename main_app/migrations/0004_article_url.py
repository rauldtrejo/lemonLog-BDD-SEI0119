# Generated by Django 3.1.7 on 2021-03-17 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
