# Generated by Django 2.1.5 on 2019-02-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0011_auto_20190203_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_public',
            field=models.BooleanField(default=True, help_text='公開かどうか', verbose_name='public status'),
        ),
    ]
