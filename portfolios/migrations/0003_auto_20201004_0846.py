# Generated by Django 3.1.1 on 2020-10-04 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_auto_20201003_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucket',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buckets', to='portfolios.portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(max_length=150, unique_for_date='created'),
        ),
    ]
