from django.urls import path,re_path
from . import views
from .views import AddUserAskView


urlpatterns=[
    #re_path(r'^$',views.index,name='index'),#$表示匹配到$结束
    re_path(r'^org_list/$',views.org_list,name='org_list'),
    re_path(r'^add_ask/$',AddUserAskView.as_view(),name='add_ask'),


]