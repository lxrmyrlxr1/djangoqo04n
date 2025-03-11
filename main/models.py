#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class menpiaoxinxi(BaseModel):
    __doc__ = u'''menpiaoxinxi'''
    __tablename__ = 'menpiaoxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是username字段，mima就是password字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的operate中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击confirm调用update接口，Revisesfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，addedthumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],addedclicktime[前端不显示该字段]字段（调用info/detail接口的时候更new），按clicktime排序Query)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表added用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是administrator，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    biaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='title' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='Cover' )
    laiyuan=models.TextField   (  null=True, unique=False, verbose_name='sources' )
    weizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='location' )
    miaoshu=models.TextField   (  null=True, unique=False, verbose_name='description' )
    dianping=models.CharField ( max_length=255, null=True, unique=False, verbose_name='review' )
    pinglun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='evaluate' )
    jiage=models.IntegerField  (  null=True, unique=False, verbose_name='price' )
    tese=models.TextField   (  null=True, unique=False, verbose_name='special' )
    kaifangshijian=models.TextField   (  null=True, unique=False, verbose_name='opentime' )
    '''
    biaoti=VARCHAR
    fengmian=Text
    laiyuan=Text
    weizhi=VARCHAR
    miaoshu=Text
    dianping=VARCHAR
    pinglun=VARCHAR
    jiage=Integer
    tese=Text
    kaifangshijian=Text
    '''
    class Meta:
        db_table = 'menpiaoxinxi'
        verbose_name = verbose_name_plural = 'ticket information'
class mingsuxinxi(BaseModel):
    __doc__ = u'''mingsuxinxi'''
    __tablename__ = 'mingsuxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是username字段，mima就是password字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的operate中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击confirm调用update接口，Revisesfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，addedthumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],addedclicktime[前端不显示该字段]字段（调用info/detail接口的时候更new），按clicktime排序Query)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表added用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是administrator，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    biaoti=models.CharField ( max_length=255, null=True, unique=False, verbose_name='title' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='Cover' )
    dizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='address' )
    pinglun=models.CharField ( max_length=255, null=True, unique=False, verbose_name='evaluate' )
    fenlei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='Classification' )
    jiage=models.IntegerField  (  null=True, unique=False, verbose_name='price' )
    pingfen=models.FloatField   (  null=True, unique=False, verbose_name='score' )
    pinglunshu=models.IntegerField  (  null=True, unique=False, verbose_name='number of ratings' )
    '''
    biaoti=VARCHAR
    fengmian=Text
    dizhi=VARCHAR
    pinglun=VARCHAR
    fenlei=VARCHAR
    jiage=Integer
    pingfen=Float
    pinglunshu=Integer
    '''
    class Meta:
        db_table = 'mingsuxinxi'
        verbose_name = verbose_name_plural = 'hotel Information'
class tejiajipiao(BaseModel):
    __doc__ = u'''tejiajipiao'''
    __tablename__ = 'tejiajipiao'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是username字段，mima就是password字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的operate中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击confirm调用update接口，Revisesfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，addedthumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],addedclicktime[前端不显示该字段]字段（调用info/detail接口的时候更new），按clicktime排序Query)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表added用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是administrator，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    chufadi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='出发地' )
    mudidi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='目的地' )
    fengjingtu=models.TextField   (  null=True, unique=False, verbose_name='风景图' )
    chufashijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='出发时间' )
    jiage=models.CharField ( max_length=255, null=True, unique=False, verbose_name='price' )
    redu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='热度' )
    biaoqian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='标签' )
    miaoshu=models.TextField   (  null=True, unique=False, verbose_name='description' )
    '''
    chufadi=VARCHAR
    mudidi=VARCHAR
    fengjingtu=Text
    chufashijian=VARCHAR
    jiage=VARCHAR
    redu=VARCHAR
    biaoqian=VARCHAR
    miaoshu=Text
    '''
    class Meta:
        db_table = 'tejiajipiao'
        verbose_name = verbose_name_plural = '特价机票'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='title' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='subtitle' )
    content=models.TextField   ( null=False, unique=False, verbose_name='context' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='picture1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='picture2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='picture3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'systemintro'
        verbose_name = verbose_name_plural = '关于我们'
