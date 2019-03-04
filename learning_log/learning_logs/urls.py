# coding=UTF-8
"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'), #名为index的URL模式
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'), #名为topics的URL模式
]
