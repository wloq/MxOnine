# _*_ coding: utf-8 _*_
from django.apps import AppConfig


class OperationConfig(AppConfig):
    name = 'operation'
    verbose_name = u"用户操作" #定义xadmin左侧菜单的中文名,还要在__init__中设置，见例子
