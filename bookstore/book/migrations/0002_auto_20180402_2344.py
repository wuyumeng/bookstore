# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name_plural': '书籍', 'verbose_name': '书籍'},
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(choices=[('JAVASCRIPT', 'javascript'), ('DATABASE', '数据库'), ('OPERATINGSYSTEM', '操作系统'), ('PYTHON', 'python'), ('ALGORITHMS', '数据结构与算法'), ('MACHINELEARNING', '机器学习')], default=1, verbose_name='商品种类'),
        ),
    ]
