# _*_ coding: utf-8 _*_
__author__ = 'wloq'
__date__ = '2019/6/9 16:33'
import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']  # 在xadmin中要显示的字段
    search_fields = ['name', 'desc']  # 后台在哪些字段中搜索
    list_filter = ['name', 'desc', 'add_time']  # 后台xadmin中在字段中过滤

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums','fav_nums','address','city']  # 在xadmin中要显示的字段
    search_fields = ['name', 'desc', 'click_nums','fav_nums','address','city'] # 后台在哪些字段中搜索
    list_filter = ['name', 'desc', 'click_nums','fav_nums','address','city__name','add_time']  # 后台xadmin中在字段中过滤

class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_year','work_company','work_position','points']  # 在xadmin中要显示的字段
    search_fields = ['org', 'name', 'work_year','work_company','work_position','points'] # 后台在哪些字段中搜索
    list_filter = ['org__name', 'name', 'work_year','work_company','work_position','points']  # 后台xadmin中在字段中过滤



xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)