# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-30 下午7:04
# @Author  : Toby
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.conf.urls import url

from  views import  (
    index,
    add,
    detail,
    list,
    search,
    delete,
    mtbftest,
    monkeytest,
    ctstest,
    ajax_smoking,


    demo_ajax,
    demo_add,

)

urlpatterns = [
    url(r'^$',index,name='rc_test_index'),
    url(r'^list/(?P<m_id>\d+)/$',list,name='list'),
    # url(r'^detail/(?P<id>)\d+/$',detail,name='detail'),
    url(r'^add/',add,name='add'),
    url(r'^search/',search,name='search'),
    url(r'^delete/',delete,name='delete'),

    url(r'^ajax_smoking/',ajax_smoking,name='ajax_smoking'),


    url(r'^demo_ajax/', demo_ajax),
    url(r'^demo_add/', demo_add),
]
