# Generated by Django 2.1.7 on 2019-02-14 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gql', '0022_auto_20190214_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='gql.Category', verbose_name='カテゴリー'),
        ),
    ]