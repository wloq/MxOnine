# _*_ coding: utf-8 _*_
from django.apps import AppConfig


class OrganizationConfig(AppConfig):
    name = 'organization'
    verbose_name = u"机构管理"  # 定义xadmin左侧菜单的中文名,还要在__init__中设置，见例子
