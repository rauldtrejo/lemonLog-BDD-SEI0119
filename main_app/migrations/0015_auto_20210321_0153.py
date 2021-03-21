# Generated by Django 3.1.7 on 2021-03-21 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20210319_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='main_app.post'),
            preserve_default=False,
        ),
    ]
