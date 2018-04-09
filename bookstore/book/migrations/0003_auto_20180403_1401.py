# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20180402_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeriInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('hcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(verbose_name='商品种类', default=1, choices=[('ALGORITHMS', '数据结构与算法'), ('OPERATINGSYSTEM', '操作系统'), ('DATABASE', '数据库'), ('JAVASCRIPT', 'javascript'), ('MACHINELEARNING', '机器学习'), ('PYTHON', 'python')]),
        ),
    ]
