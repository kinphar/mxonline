# Generated by Django 2.2 on 2021-07-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_opportunity_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='备注'),
        ),
    ]