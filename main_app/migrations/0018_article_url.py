# Generated by Django 3.1.7 on 2021-03-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_remove_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
