# Generated by Django 2.1.7 on 2019-03-24 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0023_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='place',
            field=models.TextField(blank=True, verbose_name='開催場所'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z+]*$', '小英数字+だけね')], verbose_name='タグ'),
        ),
    ]