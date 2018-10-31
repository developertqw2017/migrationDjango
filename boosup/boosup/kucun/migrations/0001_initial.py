# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('goods_name', models.CharField(max_length=15)),
                ('kadi_count', models.IntegerField()),
                ('is_lastet', models.BooleanField(default=True)),
                ('save_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeCountRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('old_count', models.IntegerField()),
                ('real_count', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('goods_name', models.CharField(max_length=15)),
                ('average_price', models.FloatField()),
                ('last_price', models.FloatField()),
                ('update_date', models.DateField(auto_now_add=True)),
                ('recent_sell', models.DateField(null=True, blank=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('add_people', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsAddRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('number', models.IntegerField()),
                ('price', models.FloatField()),
                ('remark', models.TextField(null=True, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('goods', models.ForeignKey(to='kucun.Goods', on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('change_num', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('goods', models.ForeignKey(to='kucun.Goods', on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsReturnRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsSellRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sell_num', models.IntegerField()),
                ('average_price', models.FloatField()),
                ('sell_price', models.FloatField()),
                ('is_arrears', models.BooleanField()),
                ('customer', models.CharField(default='无', max_length=10)),
                ('phonenumber', models.CharField(default='无', max_length=15)),
                ('address', models.CharField(default='无', max_length=50)),
                ('remark', models.TextField(null=True, blank=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('goods', models.ForeignKey(to='kucun.Goods', on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsShop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('remain', models.IntegerField()),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('goods', models.ForeignKey(to='kucun.Goods', on_delete = models.CASCADE)),
                ('last_updater', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='InboundChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('phonenumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('unit_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(to='kucun.GoodsShop', on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('is_arrears', models.BooleanField()),
                ('customer', models.CharField(default='无', max_length=10)),
                ('phonenumber', models.CharField(default='无', max_length=15)),
                ('address', models.CharField(default='无', max_length=50)),
                ('remark', models.TextField(null=True, blank=True)),
                ('all_price', models.FloatField(default=0)),
                ('all_profit', models.FloatField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updater', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='OtherCost',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('purpose', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('is_delete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updater', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='RefundRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sell_record', models.ForeignKey(to='kucun.GoodsSellRecord', on_delete = models.CASCADE)),
                ('updater', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('principal', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='TransferRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('count', models.IntegerField()),
                ('remark', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('goods', models.ForeignKey(to='kucun.Goods', on_delete = models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='TransferShop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('phonenumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='transferrecord',
            name='transfer_shop',
            field=models.ForeignKey(to='kucun.TransferShop', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='transferrecord',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsshop',
            name='shop',
            field=models.ForeignKey(to='kucun.Shop', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodssellrecord',
            name='order',
            field=models.ForeignKey(null=True, blank=True, to='kucun.Order', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodssellrecord',
            name='shop',
            field=models.ForeignKey(to='kucun.Shop', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodssellrecord',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsreturnrecord',
            name='goods_sell_record',
            field=models.ForeignKey(to='kucun.GoodsSellRecord', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsreturnrecord',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='shop',
            field=models.ForeignKey(to='kucun.Shop', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsaddrecord',
            name='inbound_channel',
            field=models.ForeignKey(to='kucun.InboundChannel', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsaddrecord',
            name='shop',
            field=models.ForeignKey(to='kucun.Shop', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='goodsaddrecord',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='changecountrecord',
            name='goods',
            field=models.ForeignKey(to='kucun.Goods', on_delete = models.CASCADE),
        ),
        migrations.AddField(
            model_name='changecountrecord',
            name='updater',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete = models.CASCADE),
        ),
    ]
