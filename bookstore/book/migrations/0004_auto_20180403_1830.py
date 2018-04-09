# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20180403_1401'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeriInfo',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='unite',
            new_name='unit',
        ),
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.SmallIntegerField(verbose_name='商品状态', choices=[(0, '下线'), (1, '上线')], default=1),
        ),
        migrations.AlterField(
            model_name='books',
            name='type_id',
            field=models.SmallIntegerField(verbose_name='商品种类', choices=[(1, 'python'), (2, 'javascript'), (3, '数据结构与算法'), (4, '机器学习'), (5, '操作系统'), (6, '数据库')], default=1),
        ),
    ]
