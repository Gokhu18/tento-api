# Generated by Django 2.1.5 on 2019-02-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190201_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.ForeignKey(blank=True, help_text='Specific course for this user.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='users.Course', verbose_name='コース'),
        ),
        migrations.AlterField(
            model_name='user',
            name='departments',
            field=models.ManyToManyField(blank=True, help_text='Specific Departments for this user.', related_name='users', to='users.Department', verbose_name='所属'),
        ),
        migrations.AlterField(
            model_name='user',
            name='teams',
            field=models.ManyToManyField(blank=True, help_text='Specific Departments for this user.', related_name='users', to='users.Team', verbose_name='サークル'),
        ),
    ]
