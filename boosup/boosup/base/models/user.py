'''
Created on 2016/9/16
@author: cloudy
'''

from django.db import models
from django.contrib.auth.models import AbstractUser
from .position import Position




class User(AbstractUser):
    '''用户'''

    mobile = models.CharField(max_length=20,verbose_name=u'电话',null=True,blank=True,unique=True,default='')
    short_phone = models.CharField(max_length=10,verbose_name=u'短号',null=True,blank=True,default='')
    position = models.ForeignKey(Position,related_name = 'user_positon' ,verbose_name=u'职位',null=True,blank=True, on_delete = models.CASCADE)
    username_zh = models.CharField(max_length=20,verbose_name=u'中文名称',null=True,blank=True,default='')
    department = models.ForeignKey('Department', related_name = 'user_department',verbose_name=u'部门',null=True,blank=True, on_delete = models.CASCADE)
    chief = models.ForeignKey('self', verbose_name=u'上级', related_name = 'user_chief',null=True,blank=True, on_delete = models.CASCADE)


    def __unicode__(self):
        return self.username_zh or ""

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户管理'

class Department(models.Model):
    '''部门'''
    name  = models.CharField(max_length=20,verbose_name=u"部门",null=False)
    parent  = models.ForeignKey('self',verbose_name=u"上级部门",null=True,blank=True, on_delete = models.CASCADE)
    charge = models.ForeignKey('User',related_name='charge',verbose_name=u'负责人',null=True,blank=True, on_delete = models.CASCADE)


    def __unicode__(self):
        return self.name or ''

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门管理'
