# Generated by Django 3.1.4 on 2020-12-06 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201203_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='is_relation',
        ),
    ]