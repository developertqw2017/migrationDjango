'''
Created on 2018/10/30
@author: developertqw2017
'''
from django.contrib import admin

from ..models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    '''用户后台信息管理'''
    list_display = ['name','parent','charge']
    search_fields = ['parent','charge']
    list_filter = ['parent','charge']

    fieldsets = [
        (u'基本信息',{
            'fields':['name','parent','charge'],
        }),

    ]
