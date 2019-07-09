# _*_ coding: utf-8 _*_
__author__ = 'wloq'
__date__ = '2019/6/9 15:07'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner

class BaseSetting(object):#注册全局设置,设置主题
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):#xadmin的标题和底部
    site_title = "wloq的管理系统"
    site_footer = "wloq的创业公司"
    menu_style = "accordion"#左侧菜单收起

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']#在xadmin中要显示的字段
    search_fields = ['code','email','send_type']#后台在哪些字段中搜索
    list_filter = ['code','email','send_type','send_time']#后台xadmin中在字段中过滤

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']  # 在xadmin中要显示的字段
    search_fields = ['title', 'image', 'url','index']  # 后台在哪些字段中搜索
    list_filter = ['title', 'image', 'url', 'index','add_time']  # 后台xadmin中在字段中过滤

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)#在xadmin中把EmailVerifyRecord表引入
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)#注册全局设置,注册主题
xadmin.site.register(views.CommAdminView,GlobalSettings)#页头和页脚设置