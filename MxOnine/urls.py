"""MxOnine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
import xadmin
from django.views.static import serve#显示数据库中的图片（地址）
from MxOnine.settings import MEDIA_ROOT#显示数据库中的图片（地址）


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path(r'^',include('apps.users.urls')),#表示匹配根路径
    re_path(r'^course/',include('apps.course.urls')),
    re_path(r'^organization/', include('apps.organization.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),#显示数据库中的图片（地址）






]