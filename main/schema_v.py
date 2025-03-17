# coding:utf-8
__author__ = "ila"

import logging, os, time

from django.http import JsonResponse
from django.apps import apps
from wsgiref.util import FileWrapper
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect

from .config_model import config
from util.codes import *
from util import message as mes
from util.baidubce_api import BaiDuBce
from util.locate import geocoding
from dj2.settings import dbName as schemaName
from dj2.settings import hasHadoop
from django.db import connection
from hdfs.client import Client

def schemaName_cal(request, tableName, columnName):
    '''
     Calculate the rules interface
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, 'data': []}
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:

                data = m.getcomputedbycolumn(
                    m,
                    m,
                    columnName
                )
                print(data)
                if data:
                    try:
                        sum='%.05f' % float(data.get("sum"))
                    except:
                        sum=0.00
                    try:
                        max='%.05f' % float(data.get("max"))
                    except:
                        max=0.00
                    try:
                        min='%.05f' % float(data.get("min"))
                    except:
                        min=0.00
                    try:
                        avg='%.05f' % float(data.get("avg"))
                    except:
                        avg=0.00
                    msg['data'] = {
                        "sum": sum,
                        "max": max,
                        "min": min,
                        "avg": avg,
                    }
                break

        return JsonResponse(msg)


def schemaName_file_upload(request):
    '''
    upload
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}

        file = request.FILES.get("file")

        if file:
            filename = file.name
            filesuffix = filename.split(".")[-1]
            file_name = "{}.{}".format(int(float(time.time()) * 1000), filesuffix)
            filePath = os.path.join(os.getcwd(), "templates/front", file_name)
            print("filePath===========>", filePath)

            with open(filePath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            msg["file"] = file_name
            req_dict = request.session.get("req_dict")
            type1 = req_dict.get("type", 0)
            print("type1=======>",type1)
            type1 = int(type1)
            if type1 == 1:
                params = {"name":"faceFile","value": file_name}
                config.createbyreq(config, config, params)
            if '是' in hasHadoop or 'spark' in hasHadoop:
                try:
                    client = Client("http://127.0.0.1:50070/")
                    client.upload(hdfs_path=f'/{file_name}', local_path=filePath, chunk_size=2 << 19, overwrite=True)
                except Exception as e:
                    print(f"hdfs upload error : {e}")

        return JsonResponse(msg)


def schemaName_file_download(request):
    '''
    download
    '''
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")
        filename = req_dict.get("fileName")

        filePath = os.path.join(os.getcwd(), "templates/front", filename)
        print("filePath===========>", filePath)
        if '是' in hasHadoop or 'spark' in hasHadoop:
            try:
                client = Client("http://127.0.0.1:50070/")
                client.download(hdfs_path=f'/{filename}', local_path=filename, overwrite=True)
            except Exception as e:
                print(f"hdfs download error : {e}")
        file = open(filePath, 'rb')
        response = HttpResponse(file)

        response['Content-Type'] = 'text/plain'
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(filePath)
        response['Content-Length'] = os.path.getsize(filePath)
        return response


def schemaName_follow_level(request, tableName, columnName, level, parent):
    '''

    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, 'data': []}
        # Query
        params = {
            "level": level,
            "parent": parent
        }

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:
                data = m.getbyparams(
                    m,
                    m,
                    params
                )
                # only this colum
                for i in data:
                    msg['data'].append(i.get(columnName))
                break
        return JsonResponse(msg)


def schemaName_follow(request, tableName, columnName):
    '''
    Get a single-line record interface for a table based on the option field value
    Combine columnName and columnValue into dict and pass into the Query method
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, 'data': []}
        # Query
        params = request.session.get('req_dict')
        columnValue = params.get("columnValue")
        params = {columnName: columnValue}

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:
                data = m.getbyparams(
                    m,
                    m,
                    params
                )
                if len(data)>0:
                    msg['data'] = data[0]
                break

        return JsonResponse(msg)


def schemaName_location(request):
    '''
    LOCATION
    :return:
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "address": ''}
        req_dict = request.session.get('req_dict')

        datas = config.getbyparams(config, config, {"name": "baidu_ditu_ak"})
        if len(datas) > 0:
            baidu_ditu_ak = datas[0].get("baidu_ditu_ak")
        else:
            baidu_ditu_ak = 'QvMZVORsL7sGzPyTf5ZhawntyjiWYCif'
        lat = req_dict.get("lat", 24.2943350100)
        lon = req_dict.get("lng", 116.1287866600)
        msg['address'] = geocoding(baidu_ditu_ak, lat, lon)

        return JsonResponse(msg)


def schemaName_matchface(request):
    if request.method in ["POST", "GET"]:
        try:
            msg = {"code": normal_code}
            req_dict = request.session.get("req_dict")

            face1 = req_dict.get("face1")
            file_path1 = os.path.join(os.getcwd(),"templates/front",face1)

            face2 = req_dict.get("face2")
            file_path2 = os.path.join(os.getcwd(), "templates/front", face2)

            data = config.getbyparams(config, config, {"name": "APIKey"})
            client_id = data[0].get("value")
            data = config.getbyparams(config, config, {"name": "SecretKey"})
            client_secret = data[0].get("value")

            bdb = BaiDuBce()
            score = bdb.bd_check2pic(client_id, client_secret, file_path1, file_path2)
            msg['score'] = score

            return JsonResponse(msg)
        except:
            return JsonResponse({"code": 500, "msg": "wrong", "score": 0})


def schemaName_option(request, tableName, columnName):
    '''
   Gets a field list interface for a table
    :param request:
    :param tableName:
    :param columnName:
    :return:
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, 'data': []}

        new_params = {}
        params = request.session.get("req_dict")
        if params.get('conditionColumn') != None and params.get('conditionValue') != None:
            new_params[params['conditionColumn']] = params['conditionValue']

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:
                data = m.getbyColumn(
                    m,
                    m,
                    columnName,
                    new_params
                )

                msg['data'] = data
                break
        return JsonResponse(msg)


def schemaName_remind_tablename_columnname_type(request, tableName, columnName, type)->int:
    '''
   Front desk reminder interface 
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, 'data': []}
        # Query
        params = request.session.get("req_dict")
        remindstart = int(params.get('remindstart')) if params.get('remindstart') != None else None
        remindend = int(params.get('remindend')) if params.get('remindend') != None else None
        if int(type) == 1:  # number
            if remindstart == None and remindend != None:
                params['remindstart'] = 0
            elif remindstart != None and remindend == None:
                params['remindend'] = 999999
            elif remindstart == None and remindend == None:
                params['remindstart'] = 0
                params['remindend'] = 999999
        elif int(type) == 2:  # date
            current_time = int(time.time())
            if remindstart == None and remindend != None:
                starttime = current_time - 60 * 60 * 24 * 365 * 2
                params['remindstart'] = time.strftime("%Y-%m-%d", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * remindend
                params['remindend'] = time.strftime("%Y-%m-%d", time.localtime(endtime))

            elif remindstart != None and remindend == None:
                starttime = current_time - 60 * 60 * 24 * remindstart
                params['remindstart'] = time.strftime("%Y-%m-%d", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * 365 * 2
                params['remindend'] = time.strftime("%Y-%m-%d", time.localtime(endtime))
            elif remindstart == None and remindend == None:
                starttime = current_time - 60 * 60 * 24 * 365 * 2
                params['remindstart'] = time.strftime("%Y-%m-%d", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * 365 * 2
                params['remindend'] = time.strftime("%Y-%m-%d", time.localtime(endtime))

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:
                data = m.getbetweenparams(
                    m,
                    m,
                    columnName,
                    params
                )

                msg['count'] = len(data)
                break
        return JsonResponse(msg)


def schemaName_tablename_remind_columnname_type(request, tableName, columnName, type):
    '''
    Background reminder interface to judge the permission of authSeparate and authTable
    '''
    if request.method in ["POST", "GET"]:
        print("schemaName_tablename_remind_columnname_type==============>")
        msg = {"code": normal_code, 'data': []}

        req_dict = request.session.get("req_dict")
        remindstart = int(req_dict.get('remindstart')) if req_dict.get('remindstart')!=None else None
        remindend = int(req_dict.get('remindend')) if req_dict.get('remindend')!=None else None
        print("req_dict===================>",req_dict)
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:
                tableModel=m
                break
        columns = tableModel.getallcolumn(tableModel, tableModel)

        # Table of the current login user
        tablename = request.session.get("tablename")
        #If the column attribute authTable has a value (a user table) [the column name of the column must be the same as the login field name of the user table], the corresponding table has a hidden attribute authTable "Yes", then the user can only view his own when viewing the table information
        try:
            __authTables__ =tableModel.__authTables__
        except:
            __authTables__ = {}

        if __authTables__ != {}:

            for authColumn, authTable in __authTables__.items():
                if authTable == tablename:
                    params = request.session.get("params")
                    req_dict[authColumn] = params.get(authColumn)
                    break


        '''__authSeparate__true，params add userid'''
        try:
            __authSeparate__ =tableModel.__authSeparate__
        except:
            __authSeparate__ = None

        if __authSeparate__ == "yes":
            tablename = request.session.get("tablename")
            if tablename != "users" and 'userid' in columns:
                try:
                    pass
                    # req_dict['userid'] = request.session.get("params").get("id")
                except:
                    pass

        # Query
        if int(type) == 1:  # number
            if remindstart == None and remindend != None:
                req_dict['remindstart'] = 0
            elif remindstart != None and remindend == None:
                req_dict['remindend'] = 999999
            elif remindstart == None and remindend == None:
                req_dict['remindstart'] = 0
                req_dict['remindend'] = 999999
        elif int(type) == 2:  # date
            current_time = int(time.time())
            if remindstart == None and remindend != None:
                starttime = current_time - 60 * 60 * 24 * 365 * 2
                req_dict['remindstart'] = time.strftime("%Y-%m-%d", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * remindend
                req_dict['remindend'] = time.strftime("%Y-%m-%d", time.localtime(endtime))

            elif remindstart != None and remindend == None:
                starttime = current_time + 60 * 60 * 24 * remindstart
                req_dict['remindstart'] = time.strftime("%Y-%m-%d", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * 365 * 2
                req_dict['remindend'] = time.strftime("%Y-%m-%d", time.localtime(endtime))
            elif remindstart == None and remindend == None:
                starttime = current_time - 60 * 60 * 24 * 365 * 2
                req_dict['remindstart'] = time.strftime("%Y-%m-%d", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * 365 * 2
                req_dict['remindend'] = time.strftime("%Y-%m-%d", time.localtime(endtime))
            else:
                starttime = current_time + 60 * 60 * 24 * remindstart
                req_dict['remindstart'] = time.strftime("%Y-%m-%d", time.localtime(starttime))
                endtime = current_time + 60 * 60 * 24 * remindend
                req_dict['remindend'] = time.strftime("%Y-%m-%d", time.localtime(endtime))
        print("req_dict==============>",req_dict)
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:
                data = m.getbetweenparams(
                    m,
                    m,
                    columnName,
                    req_dict
                )

                msg['count'] = len(data)
                break
        return JsonResponse(msg)

def schemaName_sh(request, tableName):
    '''
    And the sfsh status interface according to the primary key idRevisetable table
    '''
    if request.method in ["POST", "GET"]:
        print('tableName=========>', tableName)
        msg = {"code": normal_code, "msg": "success", "data": {}}
        req_dict = request.session.get("req_dict")
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:

                # Query
                data1 = m.getbyid(
                    m,
                    m,
                    req_dict.get('id')
                )
                if data1[0].get("sfsh") == 'yes':
                    req_dict['sfsh'] = 'no'
                else:
                    req_dict['sfsh'] = 'no'

                # renew
                res = m.updatebyparams(
                    m,
                    m,
                    req_dict
                )
                # logging.warning("schemaName_sh.res=====>{}".format(res))
                if res!=None:
                    msg["code"]=crud_error_code
                    msg["code"]=mes.crud_error_code
                break
        return JsonResponse(msg)


def schemaName_upload(request, fileName):
    '''
    '''
    if request.method in ["POST", "GET"]:
        return HttpResponseRedirect  ("/{}/front/{}".format(schemaName,fileName))


def schemaName_group_quyu(request, tableName, columnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        allModels = apps.get_app_config('main').get_models()
        where = {}
        for m in allModels:
            if m.__tablename__ == tableName:
                for item in m.__authTables__.items():
                    if request.session.get("tablename") == item[1]:
                        where[item[0]] = request.session.get("params").get(item[0])
                msg['data'] = m.groupbycolumnname(
                    m,
                    m,
                    columnName,
                    where
                )
                break

        return JsonResponse(msg)


def schemaName_value_quyu(request, tableName, xColumnName, yColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        allModels = apps.get_app_config('main').get_models()
        where = {}
        for m in allModels:
            if m.__tablename__ == tableName:
                for item in m.__authTables__.items():
                    if request.session.get("tablename") == item[1]:
                        where[item[0]] = request.session.get("params").get(item[0])
                msg['data'] = m.getvaluebyxycolumnname(
                    m,
                    m,
                    xColumnName,
                    yColumnName,
                    where
                )
                break

        return JsonResponse(msg)

def schemaName_value_riqitj(request, tableName, xColumnName, yColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        where = ' where 1 = 1 '
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__ == tableName:
                for item in m.__authTables__.items():
                    if request.session.get("tablename") == item[1]:
                        where = where + " and " + item[0] + " = '" +  request.session.get("params").get(item[0]) + "' "
        sql = ''
        if timeStatType == 'day':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM {3} {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, yColumnName, where, tableName, '%Y-%m-%d')

        if timeStatType == 'month':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM {3} {2} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName, yColumnName, where, tableName, '%Y-%m')

        if timeStatType == 'year':
            sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM {3} {2} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName, yColumnName, where, tableName, '%Y')

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

        return JsonResponse(msg)

def schemaName_spider(request, tableName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": []}
        os.system(cmd)

        return JsonResponse(msg)

