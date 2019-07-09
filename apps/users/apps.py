# _*_ coding: utf-8 _*_
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = u"用户信息"  # 定义xadmin左侧菜单的中文名,还要在__init__中设置，见例子
