'''
Created on 2018/10/30
@author: developertqw2017
'''

from django import forms

class loginForm(forms.Form):
    '''登录表单'''
    username  = forms.CharField(max_length=20,label=u"用户名",required=True)
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput,required=True)
