# Generated by Django 3.1.1 on 2020-09-29 04:49

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True, null=True, verbose_name='last Updated')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('privacy', models.CharField(choices=[('PVT', 'Private'), ('SHR', 'Shared'), ('PBL', 'Public')], default='PVT', max_length=10, verbose_name='Type')),
                ('whitelist', models.BooleanField(default=False)),
                ('members', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=50), blank=True, null=True, size=8)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolios.portfolio')),
            ],
        ),
    ]
