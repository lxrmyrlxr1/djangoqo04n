# coding:utf-8
__author__ = "ila"
import os,sys
from django.http import JsonResponse, HttpResponse
from django.apps import apps


def index(request):
    if request.method in ["GET", "POST"]:
        msg = {"code": 200, "msg": "success", "data": []}
        print("=================>index")
        return JsonResponse(msg)


def test(request, p1):
    if request.method in ["GET", "POST"]:
        msg = {"code": 200, "msg": "success", "data": []}
        print("=================>index  ", p1)
        return JsonResponse(msg)

def null(request,):
    if request.method in ["GET", "POST"]:
        msg = {"code": 200, "msg": "success", "data": []}
        return JsonResponse(msg)

def check_suffix(filelName,path1):
    try:
        image_data = open(path1, "rb").read()
    except:
        image_data = "no file"
    if '.js' in filelName:
        return HttpResponse(image_data, content_type="application/javascript")
    elif '.jpg' in filelName or '.jpeg' in filelName or '.png' in filelName or '.gif' in filelName:
        return HttpResponse(image_data, content_type="image/png")
    elif '.css' in filelName:
        return HttpResponse(image_data, content_type="text/css")
    elif '.ttf' in filelName or '.woff' in filelName:
        return HttpResponse(image_data, content_type="application/octet-stream")
    elif '.mp4' in filelName:
        return HttpResponse(image_data, content_type="video/mp4")
    elif '.mp3' in filelName:
        return HttpResponse(image_data, content_type="audio/mp3")
    elif '.csv' in filelName:
        return HttpResponse(image_data, content_type="application/CSV")
    elif '.doc' in filelName:
        return HttpResponse(image_data, content_type="application/msword")
    elif '.docx' in filelName:
        return HttpResponse(image_data, content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    elif '.xls' in filelName:
        return HttpResponse(image_data, content_type="application/vnd.ms-excel")
    elif '.xlsx' in filelName:
        return HttpResponse(image_data, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    elif '.ppt' in filelName:
        return HttpResponse(image_data, content_type="application/vnd.ms-powerpoint")
    elif '.pptx' in filelName:
        return HttpResponse(image_data, content_type="application/vnd.openxmlformats-officedocument.presentationml.presentation")
    elif '.zip' in filelName:
        return HttpResponse(image_data, content_type="application/x-zip-compressed")
    elif '.rar' in filelName:
        return HttpResponse(image_data, content_type="application/octet-stream")
    else:
        return HttpResponse(image_data, content_type="text/html")

def admin_lib2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/lib/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def admin_lib3(request, p1, p2, p3):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/lib/", p1, p2, p3)
        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)
  

def admin_lib4(request, p1, p2, p3, p4):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/lib/", p1, p2, p3, p4)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)
      

def admin_page(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/page/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def admin_page2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/page/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def admin_pages(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/pages/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)
       
def admin_pages2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/pages/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def admin_file1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def admin_file2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/", p1, p2)
        if not  os.path.isfile(path1):
            path1 = os.path.join(os.getcwd(), "templates/front/admin/dist/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def admin_file3(request, p1, p2, p3):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/", p1, p2, p3)

        if not  os.path.isfile(path1):
            path1 = os.path.join(os.getcwd(), "templates/front/admin/dist/", p1, p2,p3)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def admin_file4(request, p1, p2, p3, p4):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/admin/", p1, p2, p3, p4)
        if not  os.path.isfile(path1):
            path1 = os.path.join(os.getcwd(), "templates/front/admin/dist/", p1, p2,p3,p4)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def front_pages(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/pages/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def front_pages2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/pages/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def layui1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/layui/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def layui2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/layui/", p1, p2)
        print("layui2 path1========================>",path1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def layui3(request, p1, p2, p3):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/layui/", p1, p2, p3)
        print("layui3 path1========================>",path1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def layui4(request, p1, p2, p3, p4):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/layui/", p1, p2, p3, p4)
        print("layui4 path1========================>",path1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def pages1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/pages/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def pages2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/pages/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def front_file1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def front_file2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def schema_front1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def schema_front2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def schema_front3(request, p1, p2, p3):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/", p1, p2, p3)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def schema_front4(request, p1, p2, p3, p4):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/", p1, p2, p3, p4)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def assets1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/assets/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def assets2(request, p1, p2):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/assets/", p1, p2)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def assets3(request, p1, p2, p3):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/assets/", p1, p2, p3)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def assets4(request, p1, p2, p3, p4):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/assets/", p1, p2, p3, p4)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def css1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/css/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def js1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/js/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)


def img1(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/img/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)

def front_modules(request, p1):
    if request.method in ["GET", "POST"]:
        fullPath = request.get_full_path()
        print("{}=============>".format(sys._getframe().f_code.co_name), fullPath)
        path1 = os.path.join(os.getcwd(), "templates/front/modules/", p1)

        return check_suffix(eval(eval(sys._getframe().f_code.co_name).__code__.co_varnames[-3]),path1)
