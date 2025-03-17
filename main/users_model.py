# coding:utf-8
__author__ = "ila"

from django.db import models

from .model import BaseModel


class users(BaseModel):
    # id=models.BigIntegerField(verbose_name="add id")
    username = models.CharField(max_length=100, verbose_name=u'username')
    password = models.CharField(max_length=100, verbose_name=u'password')
    role = models.CharField(max_length=100, verbose_name=u'adimin')
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'creat time')
    __tablename__ = 'users'

    class Meta:
        db_table = 'users'
        verbose_name = verbose_name_plural = u'administrator'

    # def __str__(self):
    #     return self.username
