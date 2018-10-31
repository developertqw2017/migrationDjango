'''
Created on 2018/10/30
@author: developertqw2017
'''

from  django.conf.urls import url
from . import views

urlpatterns = [

        url(r'^login/$',views.login,name='login'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^settings/(\w+)/$', views.settings, name='settings'),
        url(r'js_post/(\w+)/$',views.js_post,name='js_post'),
        url(r'',views.index,name='index'),


]

