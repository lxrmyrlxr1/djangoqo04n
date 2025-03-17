# coding:utf-8
# author:ila
import base64, copy
from django.http import JsonResponse
from django.apps import apps
from util.codes import *
from util import message as mes

class Auth(object):
def authenticate(self, model, req_dict):
"""
User login, loginsuccess returns token; login failed returns failure reason
: param username: Account number
:param password:password
:return: json
"""
msg = {'code': normal_code, 'msg': mes.normal_code, 'data': {}}
tablename = model.__tablename__
encode_dict = {"tablename": tablename, "params": req_dict}
encode_str = base64.b64encode(str(encode_dict).encode("utf-8"))
msg['data']["id"] = req_dict.get("id")
msg["id"] = req_dict.get("id")
msg['token'] = encode_str.decode('utf-8')
return JsonResponse(msg)
def get_token(self, model, req_dict):
tablename=model.__tablename__
encode_dict = {"tablename":tablename, "params": req_dict}
encode_str = base64.b64encode(str(encode_dict).encode("utf8"))
return encode_str.decode('utf-8')
def identify(self, request):
"""
User authentication
: param request: The object of this request
:return: list
"""
msg = {'code': normal_code, 'msg': mes.normal_code, 'data': {}}
# header of # django was processed
token = request.META.get('HTTP_TOKEN')
if token  and token !="null":
auth_token = copy.deepcopy(token)
decode_str = base64.b64decode(auth_token).decode("utf8")
decode_str=decode_str.replace('"null"','""').replace('null','""')
decode_dict = eval(decode_str)
tablename2 = decode_dict.get("tablename")
params2 = decode_dict.get("params",{})
datas=None
allModels = apps.get_app_config('main').get_models()
for model in allModels:
if model.__tablename__ == tablename2:
datas = model.getbyparams(model, model, params2)
if not datas:
msg['code'] = username_error_code
The msg ['msg'] = 'The user information was not found'
result = msg
else:
request.session['tablename'] = tablename2
return result
