#coding:utf-8
__author__ = "ila"
import base64, copy, logging, os, sys, time, xlrd, json, datetime, configparser
from django.http import JsonResponse
from django.apps import apps
from django.db.models.aggregates import Count,Sum
from .models import menpiaoxinxi
from util.codes import *
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Q
from util.baidubce_api import BaiDuBce
from .config_model import config

from dj2.settings import executor
from util.spark_func import spark_read_mysql






def menpiaoxinxi_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")


        error = menpiaoxinxi.createbyreq(menpiaoxinxi, menpiaoxinxi, req_dict)
        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = "User already exists!"
        return JsonResponse(msg)

def menpiaoxinxi_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")

        datas = menpiaoxinxi.getbyparams(menpiaoxinxi, menpiaoxinxi, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg)
        try:
            __sfsh__= menpiaoxinxi.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='yes':
            if datas[0].get('sfsh')!='yes':
                msg['code']=other_code
                msg['msg'] = "Account locked!"
                return JsonResponse(msg)
                
        req_dict['id'] = datas[0].get('id')


        return Auth.authenticate(Auth, menpiaoxinxi, req_dict)


def menpiaoxinxi_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "exit success",
            "code": 0
        }

        return JsonResponse(msg)


def menpiaoxinxi_resetPass(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  menpiaoxinxi.getallcolumn( menpiaoxinxi, menpiaoxinxi)

        try:
            __loginUserColumn__= menpiaoxinxi.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'
        recordsParam = {}
        recordsParam[username_str] = req_dict.get("username")
        records=menpiaoxinxi.getbyparams(menpiaoxinxi, menpiaoxinxi, recordsParam)
        if len(records)<1:
            msg['code'] = 400
            msg['msg'] = 'User does not exist'
            return JsonResponse(msg)

        eval('''menpiaoxinxi.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))
        
        return JsonResponse(msg)



def menpiaoxinxi_session(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = menpiaoxinxi.getbyparams(menpiaoxinxi, menpiaoxinxi, req_dict)[0]

        return JsonResponse(msg)


def menpiaoxinxi_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"yes"})
        data=menpiaoxinxi.getbyparams(menpiaoxinxi, menpiaoxinxi, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg)

def menpiaoxinxi_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        #Get all column names
        columns=  menpiaoxinxi.getallcolumn( menpiaoxinxi, menpiaoxinxi)

        #The table where the currently logged in user is located
        tablename = request.session.get("tablename")


            #authColumn=list(__authTables__.keys())[0]
            #authTable=__authTables__.get(authColumn)

            # if authTable==tablename:
                #params = request.session.get("params")
                #req_dict[authColumn]=params.get(authColumn)

        '''__authSeparate__true，params add users id，backend Query personal data'''
        try:
            __authSeparate__=menpiaoxinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

    #When the project attribute hasMessage is "yes", the generation system automatically generates the message board table messages, and the table attribute hasMessage of the table is also set to "yes". The fields include userid (user id), username (username), content (message context), reply (reply)
    #The interface page needs to distinguish permissions. Ordinary users view their own messages and reply records, and administrators view all messages and reply records
        try:
            __hasMessage__=menpiaoxinxi.__hasMessage__
        except:
            __hasMessage__=None
        if  __hasMessage__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict["userid"]=request.session.get("params").get("id")



      # Check the table attribute isAdmin of the current table. If it is true, it is the administrator table.
      # When the table attribute isAdmin = "yes", the user table that is refreshed is also the administrator, that is, page and list can view everyone's test records (also applies to other tables)

        __isAdmin__ = None

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        # The current table also has administrator privileges.
        if  __isAdmin__ == "yes" and 'menpiaoxinxi' != 'forum':
            if req_dict.get("userid") and 'menpiaoxinxi' != 'chat':
                del req_dict["userid"]

        else:
            #For tables without administrator privileges, check whether the current table field name has userid
            if tablename!="users" and 'menpiaoxinxi'[:7]!='discuss'and "userid" in menpiaoxinxi.getallcolumn(menpiaoxinxi,menpiaoxinxi):
                req_dict["userid"] = request.session.get("params").get("id")

       #When the column attribute authTable has a value (a user table) [the column name must be consistent with the login field name of the user table], the corresponding table has a hidden attribute authTable with a value of "yes", then when the user views the table information, he can only view his own
        try:
            __authTables__=menpiaoxinxi.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={}:
            try:
                del req_dict['userid']
                # tablename=request.session.get("tablename")
                # if tablename=="users":
                    # del req_dict['userid']
                
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break

        q = Q()

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =menpiaoxinxi.page(menpiaoxinxi, menpiaoxinxi, req_dict, request, q)

        return JsonResponse(msg)

def menpiaoxinxi_autoSort(request):
    '''
  ． Intelligent recommendation function (table attributes: [intelRecom (yes/no)], addedclicktime [this field is not displayed on the front end] field (new when calling info/detail interface), sort by clicktime Query)
Used in the main information list (such as product list, new news list), just display the 5 most recently clicked or most recently added records
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in menpiaoxinxi.getallcolumn(menpiaoxinxi,menpiaoxinxi):
            req_dict['sort']='clicknum'
        elif "browseduration"  in menpiaoxinxi.getallcolumn(menpiaoxinxi,menpiaoxinxi):
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = menpiaoxinxi.page(menpiaoxinxi,menpiaoxinxi, req_dict)

        return JsonResponse(msg)


def menpiaoxinxi_list(request):
    '''
   Front page
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if req_dict.__contains__('vipread'):
            del req_dict['vipread']

        #Get all column names
        columns=  menpiaoxinxi.getallcolumn( menpiaoxinxi, menpiaoxinxi)
        #Table attributes [foreEndList] Foreground list: Similar to the default list page in the background, but placed in the foreground, No: means there is no such page, Yes: means there is such page (you can view it without logging in), Need to log in: means there is such page and you need to log in to view it
        try:
            __foreEndList__=menpiaoxinxi.__foreEndList__
        except:
            __foreEndList__=None

        if __foreEndList__=="Before":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass
        #forrEndListAuth
        try:
            __foreEndListAuth__=menpiaoxinxi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None


        #authSeparate
        try:
            __authSeparate__=menpiaoxinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="yes" and __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params",{"id":0}).get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:#Judge whether there is a userid column name
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "yes":
                if req_dict.get("userid"):
                    # del req_dict["userid"]
                    pass
            else:
                #For tables without administrator privileges, check whether the current table field name has userid
                if "userid" in columns:
                    try:
                        pass
                    except:
                            pass
        #When the column attribute authTable has a value (a user table) [the column name must be consistent with the login field name of the user table], the corresponding table has a hidden attribute authTable with a value of "yes", then when the user views the table information, he can only view his own
        try:
            __authTables__=menpiaoxinxi.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="yes":
            try:
                del req_dict['userid']
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        
        if menpiaoxinxi.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass


        q = Q()

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = menpiaoxinxi.page(menpiaoxinxi, menpiaoxinxi, req_dict, request, q)

        return JsonResponse(msg)

def menpiaoxinxi_save(request):
    '''
    backend added
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys():
            del req_dict['clicktime']
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break


        #Get all column names
        columns=  menpiaoxinxi.getallcolumn( menpiaoxinxi, menpiaoxinxi)
        if tablename!='users' and req_dict.get("userid")!=None and 'userid' in columns  and __isAdmin__!='是':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']

        error= menpiaoxinxi.createbyreq(menpiaoxinxi,menpiaoxinxi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def menpiaoxinxi_add(request):
    '''
    fronted added
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        #Get all column names
        columns=  menpiaoxinxi.getallcolumn( menpiaoxinxi, menpiaoxinxi)
        try:
            __authSeparate__=menpiaoxinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=menpiaoxinxi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="no":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']
        error= menpiaoxinxi.createbyreq(menpiaoxinxi,menpiaoxinxi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)

def menpiaoxinxi_thumbsup(request,id_):
    '''
     Like: table attribute thumbsUp [yes/no], refresh the table addedthumbsupnum likes and crazilynum dislikes fields,
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=menpiaoxinxi.getbyid(menpiaoxinxi,menpiaoxinxi,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#yes
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#no
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = menpiaoxinxi.updatebyparams(menpiaoxinxi,menpiaoxinxi, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def menpiaoxinxi_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = menpiaoxinxi.getbyid(menpiaoxinxi,menpiaoxinxi, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
        #Number of views and clicks
        try:
            __browseClick__= menpiaoxinxi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="yes"  and  "clicknum"  in menpiaoxinxi.getallcolumn(menpiaoxinxi,menpiaoxinxi):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}
            ret=menpiaoxinxi.updatebyparams(menpiaoxinxi,menpiaoxinxi,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg)

def menpiaoxinxi_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =menpiaoxinxi.getbyid(menpiaoxinxi,menpiaoxinxi, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")

        #Number of views and clicks
        try:
            __browseClick__= menpiaoxinxi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="yes"   and  "clicknum"  in menpiaoxinxi.getallcolumn(menpiaoxinxi,menpiaoxinxi):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}

            ret=menpiaoxinxi.updatebyparams(menpiaoxinxi,menpiaoxinxi,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = retfo
        return JsonResponse(msg)


def menpiaoxinxi_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if req_dict.get("mima") and "mima" not in menpiaoxinxi.getallcolumn(menpiaoxinxi,menpiaoxinxi) :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in menpiaoxinxi.getallcolumn(menpiaoxinxi,menpiaoxinxi) :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = menpiaoxinxi.updatebyparams(menpiaoxinxi, menpiaoxinxi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def menpiaoxinxi_delete(request):
    '''
    batch deleted
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=menpiaoxinxi.deletes(menpiaoxinxi,
            menpiaoxinxi,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def menpiaoxinxi_vote(request,id_):
    '''
   Browsing click count (table attribute [browseClick: yes/no], click field (clicknum), backend automatically +1 when calling info/detail interface), voting function (table attribute [vote: yes/no], voting field (votenum), backend vote+1 when calling vote interface)
total number of clicks on products or news; provide voting function for news
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= menpiaoxinxi.getbyid(menpiaoxinxi, menpiaoxinxi, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=menpiaoxinxi.updatebyparams(menpiaoxinxi,menpiaoxinxi,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)

def menpiaoxinxi_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}

        excel_file = request.FILES.get("file", "")
        file_type = excel_file.name.split('.')[1]
        
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows
            
            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    menpiaoxinxi.createbyreq(menpiaoxinxi, menpiaoxinxi, req_dict)
                    
            except:
                pass
                
        else:
            msg = {
                "msg": "type wrong",
                "code": 500
            }
                
        return JsonResponse(msg)

def menpiaoxinxi_sendemail(request):
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")

        code = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)
        to = []
        to.append(req_dict['email'])

        send_mail('User Registration', 'Your registration verification code is ['+''.join(code)+'], please do not disclose the verification code to others, and do not operate it if you are not yourself. ', 'yclw9@qq.com', to, fail_silently = False)

        cursor = connection.cursor()
        cursor.execute("insert into emailregistercode(email,role,code) values('"+req_dict['email']+"','用户','"+''.join(code)+"')")

        msg = {
            "msg": "send success",
            "code": 0
        }

        return JsonResponse(msg)

# Recommendation algorithm interface
def menpiaoxinxi_autoSort2(request):
    
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")
        cursor = connection.cursor()
        leixing = set()
        try:
            cursor.execute("select inteltype from storeup where userid = %d"%(request.session.get("params").get("id"))+" and tablename = 'menpiaoxinxi' order by addtime desc")
            rows = cursor.fetchall()
            for row in rows:
                for item in row:
                    if item != None:
                        leixing.add(item)
        except:
            leixing = set()
        
        L = []
        cursor.execute("select * from menpiaoxinxi where $intelRecomColumn in ('%s"%("','").join(leixing)+"') union all select * from menpiaoxinxi where $intelRecomColumn not in('%s"%("','").join(leixing)+"')")
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)


        return JsonResponse({"code": 0, "msg": '',  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":5,"list": L[0:int(req_dict["limit"])]}})

def menpiaoxinxi_value(request, xColumnName, yColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        
        where = ' where 1 = 1 '
        sql = ''
        if timeStatType == 'day':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM menpiaoxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d') LIMIT 10".format(xColumnName, yColumnName, where, '%Y-%m-%d')

        if timeStatType == 'month':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM menpiaoxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m') LIMIT 10".format(xColumnName, yColumnName, where, '%Y-%m')

        if timeStatType == 'year':
            sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM menpiaoxinxi {2} GROUP BY DATE_FORMAT({0}, '%Y') LIMIT 10".format(xColumnName, yColumnName, where, '%Y')

        func_name = sys._getframe().f_code.co_name
        table_name = func_name.split('_')[0]
        json_filename=f'{table_name}_value_{xColumnName}_{yColumnName}.json'
        if os.path.exists(json_filename) == True:
            with open(json_filename, encoding='utf-8') as f:
                msg['data'] = json.load(f)
        else:
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'] = L
        executor.submit(spark_read_mysql, f"({sql}) {table_name}", json_filename)
        return JsonResponse(msg)

def menpiaoxinxi_o_value(request, xColumnName, yColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        
        where = ' where 1 = 1 '
        
        sql = "SELECT {0}, sum({1}) AS total FROM menpiaoxinxi {2} GROUP BY {0} LIMIT 10".format(xColumnName, yColumnName, where)
        func_name = sys._getframe().f_code.co_name
        table_name = func_name.split('_')[0]
        json_filename =  f'{table_name}_o_value_{xColumnName}_{yColumnName}.json'
        if os.path.exists(json_filename) == True:
            with open(json_filename, encoding='utf-8') as f:
                msg['data'] = json.load(f)
        else:
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'] = L
        executor.submit(spark_read_mysql, f"({sql}) {table_name}", json_filename)
        return JsonResponse(msg)




def menpiaoxinxi_count(request):
    '''
    Total number of interfaces
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = request.session.get("req_dict")
        where = ' where 1 = 1 '
        for key in req_dict:
            if req_dict[key] != None:
                where = where + " and key like '{0}'".format(req_dict[key])
        
        sql = "SELECT count(*) AS count FROM menpiaoxinxi {0}".format(where)
        count = 0
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            count = online_dict['count']
        msg['data'] = count

        return JsonResponse(msg)


def menpiaoxinxi_group(request, columnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        
        where = ' where 1 = 1 '

        sql = "SELECT COUNT(*) AS total, " + columnName + " FROM menpiaoxinxi " + where + " GROUP BY " + columnName + " LIMIT 10"

        func_name = sys._getframe().f_code.co_name
        table_name = func_name.split('_')[0]

        json_filename=f'{table_name}_group_{columnName}.json'
        if os.path.exists(json_filename)==True:
            with open(json_filename,encoding='utf-8') as f:
                msg['data']=json.load(f)
        else:
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime("%Y-%m-%d")
                    else:
                        pass
                L.append(online_dict)
            msg['data'] = L
        executor.submit(spark_read_mysql, f"({sql}) {table_name}",json_filename)
        return JsonResponse(msg)









