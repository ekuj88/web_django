# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProjectList(models.Model):
    """
    项目信息表,跟手机形成一对多的关系
    """
    P_id = models.AutoField(primary_key=True)
    P_name = models.CharField(max_length=20)     #项目表

    def __repr__(self):
        return "ProjectList  <id= %s------p_name = %s >" %(self.P_id,self.P_name)


class PhoneMsg(models.Model):
    """
    手机信息表
    """
    M_id = models.AutoField(primary_key=True)
    M_name =models.CharField(max_length=10)
    projectlist = models.ForeignKey(ProjectList,related_name='ProjectList', null=True)       #这里跟项目表形成一对多的关系
    result = models.ManyToManyField('Result')                                   #跟结果表形成多对多关系

    def __repr__(self):
        return  'PhoneMsg<M_id =%s ,M_name = %s,prolist =%s result=%s>' %(self.M_id,self.M_name,self.projectlist,self.result)

class PhoneDetail(models.Model):
    """
    """
    M_id = models.OneToOneField('PhoneMsg')      #一对一的关系
    version =models.CharField(max_length=10)
    sdk = models.CharField(max_length=10)

    def __str__(self):
        return 'PhoneDetail<id = %s ,version= %s,sdk=%s>' %(self.M_id,self.version,self.sdk)

class Result(models.Model):
    """
    结果信息表
    """
    R_id = models.AutoField(primary_key=True)                       #编号id
    R_name = models.CharField(max_length=20,null=False)             #测试case名称
    R_version=models.CharField(max_length=20,null=False)            #测试版本
    R_context = models.CharField(max_length=100,null=False)         #测试内容
    R_result= models.CharField(max_length=20,null=False)            #测试结果
    R_note = models.CharField(max_length=50,null=False)             #备注
    R_createtime = models.DateTimeField("创建时间",auto_now_add=True)#自动添加时间
    R_projectname = models.CharField(max_length=20,default='')      #手机名称
    R_ower = models.CharField(max_length=20)                        #测试机编号
    R_kexuan= models.CharField(max_length=20,default='')            #可选或者是必选项
    R_inning = models.CharField(max_length=10,default='')                      #第几轮


    # def __repr__(self):
    #     return "Result{ 'R_id ','R_name','R_version','R_context','R_result','R_note','R-time'}" %(self.R_id,self.R_name,self.R_version,self.R_context,self.R_result,self.R_note,self.R_createtime)
    def __repr__(self):
        return 'Result<R_id=%s,R_name=%s,R_version=%s,R_context=%s>' %(self.R_id,self.R_name,self.R_version,self.R_context)


