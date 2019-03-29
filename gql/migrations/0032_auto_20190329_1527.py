# Generated by Django 2.1.7 on 2019-03-29 06:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0031_auto_20190328_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=150, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Zぁ-んァ-ヶー一-龠]*$', '大小英数字+だけね')], verbose_name='タグ'),
        ),
    ]