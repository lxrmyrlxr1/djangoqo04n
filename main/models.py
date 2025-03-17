#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class menpiaoxinxi(BaseModel):
    __doc__ = u'''menpiaoxinxi'''
    __tablename__ = 'menpiaoxinxi'



    __authTables__={}
    __authPeople__= 'No' # User table, the value corresponding to the table attribute loginUserColumn is the username field, and ma is the password field
    __ Sfsh __ = 'no' # table sfsh ("audit," yes "or" no ") field and sfhf (audit reply) field, the background list (page) operate to a" audit "button, click" audit "pop up a page, including" whether "audit" and "audit reply", click confirm call update interface, Revisesfsh and sfhf two fields.
    __authSeparate__= 'No' # background list permission
    __thumbsUp__= 'No' # Table properties thumbsUp [Yes / No], addedthumbsupnum Like and crazilynum step fields
    __intelRecom__= 'No' # Intelligent recommendation function (table attribute: [intelRecom (Yes / No)], addedclicktime [front end does not display this field] field (more new when calling info / detail interface), sort Query by clicktime)
    __browseClick__= 'No' # Table attribute [browseClick: Yes / No], click the field (clicknum), the back end automatically + 1 when calling the info / detail interface), voting function (table attribute [vote: Yes / No), voting field (votenum), call the vote interface back end votenum + 1
    __foreEndListAuth__= 'No' # Foreground list permission foreEndListAuth [Yes / No]; when foreEndListAuth= Yes, brush the table assigned user field userid, the foreground list list interface can only view its own record and the background value userid of the add interface
    __foreEndList__= 'Yes' # table property [foreEndList] front ground list: similar to the background default list list page, only in the front desk, no: without this page, yes: means this page (do not need to log in to view), before login: means this page and need to log in to view
    __isAdmin__= 'No' # table attribute isAdmin= "Yes", the generated user table is also administrator, namely page and list can view all the test records (while applied to other tables)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'creat time')
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
    __authPeople__= 'No' # User table, the value corresponding to the table attribute loginUserColumn is the username field, and ma is the password field
    __ Sfsh __ = 'no' # table sfsh ("audit," yes "or" no ") field and sfhf (audit reply) field, the background list (page) operate to a" audit "button, click" audit "pop up a page, including" whether "audit" and "audit reply", click confirm call update interface, Revisesfsh and sfhf two fields.
    __authSeparate__= 'No' # background list permission
    __thumbsUp__= 'No' # Table properties thumbsUp [Yes / No], addedthumbsupnum Like and crazilynum step fields
    __intelRecom__= 'No' # Intelligent recommendation function (table attribute: [intelRecom (Yes / No)], addedclicktime [front end does not display this field] field (more new when calling info / detail interface), sort Query by clicktime)
    __browseClick__= 'No' # Table attribute [browseClick: Yes / No], click the field (clicknum), the back end automatically + 1 when calling the info / detail interface), voting function (table attribute [vote: Yes / No), voting field (votenum), call the vote interface back end votenum + 1
    __foreEndListAuth__= 'No' # Foreground list permission foreEndListAuth [Yes / No]; when foreEndListAuth= Yes, brush the table assigned user field userid, the foreground list list interface can only view its own record and the background value userid of the add interface
    __foreEndList__= 'Yes' # table property [foreEndList] front ground list: similar to the background default list list page, only in the front desk, no: without this page, yes: means this page (do not need to log in to view), before login: means this page and need to log in to view
    __isAdmin__= 'No' # table attribute isAdmin= "Yes", the generated user table is also administrator, namely page and list can view all the test records (while applied to other tables)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'craeat time')
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
    __authPeople__= 'No' # User table, the value corresponding to the table attribute loginUserColumn is the username field, and ma is the password field
    __ Sfsh __ = 'no' # table sfsh ("audit," yes "or" no ") field and sfhf (audit reply) field, the background list (page) operate to a" audit "button, click" audit "pop up a page, including" whether "audit" and "audit reply", click confirm call update interface, Revisesfsh and sfhf two fields.
    __authSeparate__= 'No' # background list permission
    __thumbsUp__= 'No' # Table properties thumbsUp [Yes / No], addedthumbsupnum Like and crazilynum step fields
    __intelRecom__= 'No' # Intelligent recommendation function (table attribute: [intelRecom (Yes / No)], addedclicktime [front end does not display this field] field (more new when calling info / detail interface), sort Query by clicktime)
    __browseClick__= 'No' # Table attribute [browseClick: Yes / No], click the field (clicknum), the back end automatically + 1 when calling the info / detail interface), voting function (table attribute [vote: Yes / No), voting field (votenum), call the vote interface back end votenum + 1
    __foreEndListAuth__= 'No' # Foreground list permission foreEndListAuth [Yes / No]; when foreEndListAuth= Yes, brush the table assigned user field userid, the foreground list list interface can only view its own record and the background value userid of the add interface
    __foreEndList__= 'No' # Table property [foreEndList] Front ground list: similar to the background default list list page, but in the front ground, no: without this page, yes: means this page (do not need to log in to view), before: means this page and need to log in to view
    __isAdmin__= 'No' # table attribute isAdmin= "Yes", the generated user table is also administrator, namely page and list can view all the test records (while applied to other tables)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'creat time')
    chufadi=models.CharField (max_length=255, null = True, unique=False, verbose_name= 'starting point')
    mudidi=models.CharField (max_length=255, null = True, unique=False, verbose_name= 'destination')
    fengjingtu=models.TextField   (  null=True, unique=False, verbose_name='Landscape map' )
    chufashijian=models.CharField (max_length=255, null = True, unique=False, verbose_name= 'departure time')
    jiage=models.CharField ( max_length=255, null=True, unique=False, verbose_name='price' )
    redu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='heat' )
    biaoqian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='label' )
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
        verbose_name = verbose_name_plural = 'lower price'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'creat time')
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
        verbose_name = verbose_name_plural = 'about us'
