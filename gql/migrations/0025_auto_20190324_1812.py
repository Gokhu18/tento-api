# Generated by Django 2.1.7 on 2019-03-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0024_auto_20190324_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='place',
            field=models.CharField(blank=True, max_length=100, verbose_name='開催場所'),
        ),
    ]
