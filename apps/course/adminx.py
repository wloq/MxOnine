# _*_ coding: utf-8 _*_
__author__ = 'wloq'
__date__ = '2019/6/9 15:53'
#在xadmin中关联注册表

import xadmin
from .models import Course,Lesson,CourseResource,Video

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_time','students']#在xadmin中要显示的字段
    search_fields = ['name','desc','detail','degree','learn_time','students']#后台在哪些字段中搜索
    list_filter = ['name','desc','detail','degree','learn_time','students']#后台xadmin中在字段中过滤

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']  # 在xadmin中要显示的字段
    search_fields = ['course', 'name', 'add_time'] # 后台在哪些字段中搜索
    list_filter = ['course__name', 'name', 'add_time']  # 后台xadmin中在字段中过滤

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']  # 在xadmin中要显示的字段
    search_fields = ['lesson', 'name', 'add_time'] # 后台在哪些字段中搜索
    list_filter = ['lesson', 'name', 'add_time']  # 后台xadmin中在字段中过滤

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time']  # 在xadmin中要显示的字段
    search_fields = ['course', 'name', 'add_time'] # 后台在哪些字段中搜索
    list_filter = ['course', 'name', 'add_time']  # 后台xadmin中在字段中过滤


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
