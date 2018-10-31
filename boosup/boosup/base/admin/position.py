'''
Created on 2018/10/30
@author: developertqw2017
'''
from django.contrib import admin

from ..models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    '''用户后台信息管理'''
    search_fields = ['name']
    list_display = ['name']
