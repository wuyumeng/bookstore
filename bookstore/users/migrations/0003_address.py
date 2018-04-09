# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180402_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('isdelete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('updata_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('recipient_name', models.CharField(verbose_name='收货人', max_length=20)),
                ('recipient_addr', models.CharField(verbose_name='收货地址', max_length=256)),
                ('recipient_phone', models.CharField(verbose_name='联系电话', max_length=11)),
                ('zip_code', models.CharField(verbose_name='邮政编码', max_length=6)),
                ('is_default', models.BooleanField(verbose_name='是否默认', default=False)),
                ('passport', models.ForeignKey(verbose_name='账户', to='users.Passport')),
            ],
            options={
                'verbose_name': '收货地址',
                'db_table': 's_user_address',
                'verbose_name_plural': '收货地址',
            },
        ),
    ]
