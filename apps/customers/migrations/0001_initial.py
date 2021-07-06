# Generated by Django 2.2 on 2021-07-06 21:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='公司名称')),
                ('address', models.CharField(max_length=150, verbose_name='公司地址')),
                ('desc', models.TextField(max_length=100, verbose_name='备注')),
                ('category', models.CharField(choices=[('zd', '终端客户'), ('jcs', '集成商')], default='zd', max_length=3, verbose_name='类型')),
                ('image', models.ImageField(upload_to='customers/%Y/%m', verbose_name='公司logo')),
            ],
            options={
                'verbose_name': '目标公司',
                'verbose_name_plural': '目标公司',
            },
        ),
        migrations.CreateModel(
            name='KeyPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('mobile', models.CharField(max_length=11, verbose_name='电话')),
                ('come_from', models.CharField(max_length=50, verbose_name='哪里人')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
                ('desc', models.CharField(max_length=100, verbose_name='备注')),
                ('image', models.ImageField(upload_to='customers/%Y/%m', verbose_name='照片')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Company', verbose_name='公司')),
            ],
            options={
                'verbose_name': '关键人物',
                'verbose_name_plural': '关键人物',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('status', models.CharField(choices=[('wbb', '未报备'), ('bbz', '报备中'), ('ybb', '已报备'), ('bbcq', '报备超期')], default='wbb', max_length=4, verbose_name='报备状态')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Company', verbose_name='公司')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.KeyPerson', verbose_name='关键人物')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='产品')),
            ],
            options={
                'verbose_name': '销售机会',
                'verbose_name_plural': '销售机会',
            },
        ),
    ]
