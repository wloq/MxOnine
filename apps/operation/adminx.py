# _*_ coding: utf-8 _*_
__author__ = 'wloq'
__date__ = '2019/6/9 18:37'

import xadmin
from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse

class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name']  # 在xadmin中要显示的字段
    search_fields = ['name', 'mobile', 'course_name'] # 后台在哪些字段中搜索
    list_filter = ['name', 'mobile', 'course_name']  # 后台xadmin中在字段中过滤

class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments']  # 在xadmin中要显示的字段
    search_fields = ['user', 'course', 'comments'] # 后台在哪些字段中搜索
    list_filter = ['user', 'course', 'comments']   # 后台xadmin中在字段中过滤

class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type']  # 在xadmin中要显示的字段
    search_fields = ['user', 'fav_id', 'fav_type'] # 后台在哪些字段中搜索
    list_filter = ['user', 'fav_id', 'fav_type']   # 后台xadmin中在字段中过滤

class UserMessageAdmin(object):
    list_display = ['user', 'message']  # 在xadmin中要显示的字段
    search_fields = ['user', 'message'] # 后台在哪些字段中搜索
    list_filter = ['user', 'message']  # 后台xadmin中在字段中过滤

class UserCourseAdmin(object):
    list_display = ['user', 'course']  # 在xadmin中要显示的字段
    search_fields = ['user', 'course']  # 后台在哪些字段中搜索
    list_filter = ['user', 'course']   # 后台xadmin中在字段中过滤

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)