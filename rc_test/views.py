# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse

from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
from .models import ProjectList,PhoneMsg,PhoneDetail,Result
# Create your views here.

import json
from django.core import serializers

def table(request):
    """
    表格页面
    :param request:
    :return:
    """
    return  render(request,'rc_test/detail.html')

def detail(request,id):
    """
    detail 详情页
    :param request:
    :return:
    """
    phoneid = PhoneMsg.objects.get(M_id = id)
    return render(request,'rc_test/detail.html',phoneid)


def revseetoindex(request):
    '''
    跳转到主页
    :param request:
    :return:
    '''
    return  HttpResponseRedirect(reverse("rc_test_index"))


def index(request):
    """
    主页
    :param request:
    :return:
    """
    # 这是id=1是国内机器
    phonelist =PhoneMsg.objects.filter(projectlist=1)
    # phonelist =PhoneMsg.objects.all()
    # print phonelist
    dict_phone={}
    dict_phone['phonelist']=phonelist

    # # 这是id=2是海外机器
    phonelist2 =PhoneMsg.objects.filter(projectlist=2)
    # print phonelist2
    dict_phone2={}
    dict_phone2['phonelist2']=phonelist2

    return  render(request,'rc_test/index.html',context={'phonelist':phonelist,
                                                       'phonelist2':phonelist2

                                                            })
def list(request,m_id=0):
    """
    list  列表页
    :param request:
    :return:
    """
    # 这是id=1是国内机器
    phonelist =PhoneMsg.objects.filter(projectlist=1)
    # phonelist =PhoneMsg.objects.all()
    # print phonelist
    dict_phone={}
    dict_phone['phonelist']=phonelist

    # # 这是id=2是海外机器
    phonelist2 =PhoneMsg.objects.filter(projectlist=2)
    # print phonelist2
    dict_phone2={}
    dict_phone2['phonelist2']=phonelist2

    id = PhoneMsg.objects.get(M_id = m_id)
    return  render(request,'rc_test/list.html',context={
                                                'phonelist':phonelist,
                                                'phonelist2':phonelist2,
                                                'name':id.M_name,
                                                'id':id.M_id,
                                                })


def ajax_smoking(request):
    '''
    主要用于ajax请求 ,获取到数据库的信息发送给前端界面显示
    :param request:
    :return: json
    '''
    if request.method=='GET':
        pid=request.GET.get('pid','')      #id
        name=request.GET.get('pname','')    #手机名称
        case=request.GET.get('id','')        #测试的case项目
        print(pid+"-- get---"+name +'----'+ case)

        p1 = PhoneMsg.objects.get(M_name=name)    #先找到这个手机型号的结果
        p2 = p1.result.filter(R_name__icontains=case).all()  #指定查找的内容是什么

        print(p1.result.all())
        print(p2)

        data = serializers.serialize('json',p2)   #在这里要把queset的对象全部转化为字符串
        rs = {'status':True,'message':data}

        return JsonResponse(rs)


        # return HttpResponse('get请求获取失败') #这里不能使用这种 ,一定要有数据返回的类型才可以 .
    elif request.method=='POST':
        usr = request.POST.get('usr','')
        print(usr+"post")
        if usr:
            ret={'status':False,'message':'nothing'}
            return HttpResponse(json.dumps(ret))
            # return HttpResponse('post请求获取succ')
        else:
            return HttpResponse('post请求获取fail')
    else:
        usr = request.POST.get('usr','')
        print(usr+"ajax")
        return HttpResponse('ajax')




def demo_ajax(request):
    return render(request, 'rc_test/demo_ajax.html')

def demo_add(request):
    a=request.GET['a']
    b=request.GET['b']

    if request.is_ajax():
        ajax_string = 'ajax request: '
    else:
        ajax_string = 'not ajax request: '

    c = int(a) + int(b)
    r = HttpResponse(ajax_string + str(c))
    return r










def add(request):
    """
    向数据库中添加数据
    :param request:
    :return:
    """
    # p1= ProjectList(P_name='内研')
    # p2= ProjectList(P_name='海外')
    # p1.save()
    # p2.save()                  #项目表

    # m1=PhoneMsg(M_name='1837')
    # m2=PhoneMsg(M_name='1830')
    # p1 = ProjectList.objects.get(P_id= 2)
    # m1.projectlist =p1          #手机表     一对多
    # m2.projectlist =p1          #手机表     一对多
    # M2=PhoneMsg(M_name='1689')
    # M2.projectlist =p1          #手机表
    # m3=PhoneMsg(M_name='1689')
    # m3.projectlist =p1          #手机表
    # m1.save()
    # m2.save()
    # m3.save()
    #
    # r1=Result(R_name='cts',R_version='35',R_context='CTS context',R_result='suc',R_note='nothing')
    # M1 = PhoneMsg.objects.first()
    # r1.save()
    # M1.result.add(r1)
    # r2=Result(R_name='Monkey',R_version='36',R_context='monkey context',R_result='suc',R_note='nothing')
    # M1 = PhoneMsg.objects.first()
    # r2.save()
    # M1.result.add(r2)
    #
    # r3=Result(R_name='Smoking',R_version='36',R_context='Smoking context',R_result='suc',R_note='nothing')
    # M1 = PhoneMsg.objects.first()
    # r3.save()
    # M1.result.add(r3)
    #
    # r4=Result(R_name='Mtbf',R_version='36',R_context='Mtbf context',R_result='suc',R_note='nothing')
    # M1 = PhoneMsg.objects.first()
    # r4.save()
    # M1.result.add(r4)
    #
    # r5=Result(R_name='python',R_version='36',R_context='python context',R_result='suc',R_note='nothing',R_projectname='1601')
    # M1 = PhoneMsg.objects.get(M_id = 2)
    # r5.save()
    # M1.result.add(r5)

    return  HttpResponse("添加数据demo成功!")


def search(request):
    """
    查询
    :param request:
    :return:
    """
    rs = PhoneMsg.objects.all()[0]
    print(rs.result.all())

    pj = ProjectList.objects.all()[1]
    print(pj.P_name)
    return HttpResponse('search over')


def delete(request):
    '''
    删除信息表
    :param request:
    :return:
    '''

    return  HttpResponse('delete over')




def presstest(request,id =1):
    '''
    压力测试
    :param request:
    :param id:
    :return:
    '''
    return HttpResponse('压力测试点击')

def ctstest(request,id=0):
    '''
    cts测试结果输出
    :param request:
    :param id:
    :return:
    '''
    return HttpResponse('ctstest')


def mtbftest(request):
    '''
    mtbf 测试结果
    :param request:
    :param id:
    :return:
    '''
    uname = 'lalalla'
    return JsonResponse({'u':uname})

def monkeytest(request,id=0):
    '''
    monkeytest
    :param request:
    :param id:
    :return:
    '''
    return HttpResponse('monkeytest')