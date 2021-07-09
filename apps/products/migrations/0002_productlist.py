# Generated by Django 2.2 on 2021-07-08 21:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('num', models.CharField(default='produce_list_/%Y/%m/%d/%H/%M/%S', max_length=30, verbose_name='编号')),
                ('count', models.IntegerField(default=1, verbose_name='数量')),
                ('discount', models.IntegerField(default=0, verbose_name='折扣')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '配置清单',
                'verbose_name_plural': '配置清单',
            },
        ),
    ]
