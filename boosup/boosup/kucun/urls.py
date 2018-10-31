# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

__author__ = 'JiaPan'

urlpatterns = [
                       url('^$', views.all_goods),

                       url('^all/goods/$', views.all_goods, name='all_goods'),
                       # url('^guoao/phone/$', views.guoao_phone, name='guoaophone'),
                       # url('^dadian/phone/$', views.dadian_phone, name='dadianphone'),
                       # url('^hongwei/phone/$', views.hongwei_phone, name='hongweiphone'),
                       #
                       # url('^all/peijian/$', views.all_peijian, name='allpeijian'),
                       # url('^guoao/peijian/$', views.guoao_peijian, name='guoaopeijian'),
                       # url('^dadian/peijian/$', views.dadian_peijian, name='dadianpeijian'),
                       # url('^hongwei/peijian/$', views.hongwei_peijian, name='hongweipeijian'),
                       #
                       url('^add/$', views.add_goods, name="addgoods"),
                       url('^add/success/$', views.add_success, name="addsuccess"),
                       url('^make_order/$', views.make_order, name="make_order"),
                       url('^inbound_channel/$', views.inbound_channel, name="inbound_channel"),
                       url('^transfer_shop_manage/$', views.transfer_shop_manage, name="transfer_shop_manage"),
                       url('^login/$', views.mylogin, name='mylogin'),
                       url('^login/fail$', views.login_fail, name='login_fail'),
                       url('^logout/$', views.mylogout, name="logout"),
                       #
                       url('^api/sell/$', views.api_sell, name="api_sell"),
                       url('^api/transfer/$', views.api_transfer, name="api_transfer"),
                       url('^api/delete_sell_record/$', views.delete_sell_record, name="delete_sell_record"),
                       url('^api/delete_order_record/$', views.delete_order_record,
                           name="delete_order_record"),
                       url('^api/add/$', views.api_add, name="api_add"),
                       url('^api/sell_info/$', views.api_sell_info, name="api_sell_info"),
                       url('^api/order_info/$', views.api_order_info, name="api_order_info"),
                       url('^api/order_list/$', views.api_order_list, name="api_order_list"),
                       url('^api/change_arrears/$', views.api_change_arrears, name="api_change_arrears"),
                       url('^api/change_order_arrears/$', views.api_change_order_arrears,
                           name="api_change_order_arrears"),
                       # url('^api/diaoku/$', views.api_diaoku, name="api_diaoku"),
                       url('^api/update/$', views.api_update, name="api_update"),
                       url('^api/update_count/$', views.api_update_count, name="api_update_count"),
                       url('^api/add_cart/$', views.add_cart, name="add_cart"),
                       url('^api/clean_cart', views.clean_cart, name="clean_cart"),
                       url('^api/delete_cart', views.delete_cart, name="delete_cart"),
                       url('^api/submit_cart', views.submit_cart, name="submit_cart"),
                       url('^api/delete_inbound', views.delete_inbound, name="delete_inbound"),
                       url('^api/delete_goods', views.delete_goods, name="delete_goods"),
                       url('^api/delete_transfer_shop', views.delete_transfer_shop, name="delete_transfer_shop"),
                       #
                       url('^outin/$', views.out_in, name="out_in"),
                       url('^out/$', views.out, name="out"),
                       url('^in/$', views.in_, name="in"),
                       url('^sell_record/$', views.sell_record, name="sell_record"),
                       url('^add_record/$', views.add_record, name="add_record"),
                       url('^today_profit/$', views.today_profit, name="today_profit"),
                       url('^yesterday_profit/$', views.yesterday_profit, name="yesterday_profit"),
                       url('^this_month_profit/$', views.this_month_profit, name="this_month_profit"),
                       url('^last_month_profit/$', views.last_month_profit, name="last_month_profit"),
                       url('^other_month_profit/$', views.other_month_profit, name="other_month_profit"),
                       url('^all_arrears/$', views.all_arrears, name="all_arrears"),
                       url('^order_arrears/$', views.order_arrears, name="order_arrears"),
                       url('^order_manage/$', views.order_manage, name="order_manage"),
                       url('^goods_return_record/$', views.goods_return_record, name="goods_return_record"),
                       url('^goods_transfer_record/$', views.transfer_record, name="transfer_record"),
                       url('^other_cost/$', views.other_cost, name="other_cost"),
                       url('^delete_goods/$', views.delete_goods, name="delete_goods"),

                       url('arrears/(\d+)/(\d+)/$', views.check_month_arrears, name='check_month_arrears'),


                       # url('^checkoutin/$', views.check_out_in, name="check_out_in"),
                       # url('^transfer/$', views.transfer, name="transfer"),
                       # url('^changeprice/$', views.change_price, name="change_price"),
                       #
                       # url('^checkbackup/$', views.check_backup, name="check_backup"),
                       # url('^backup/$', views.mybackup, name="backup"),

                       # url('^modal/diaoku/$', views.modal_diaoku, name="modal_diaoku"),
                       url('^cart_show', views.cart_show, name="cart_show"),

                       url('^chart/profit/$', views.profit_chart, name="profit_chart"),
                       url('^chart/sell_ranking/$', views.sell_ranking_chart, name="sell_ranking_chart"),
]
