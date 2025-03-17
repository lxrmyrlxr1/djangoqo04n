# coding:utf-8
__author__ = "ila"

from django.db import models

from .model import BaseModel


class config(BaseModel):
    # id=models.BigIntegerField(verbose_name="add id")
    name = models.CharField(max_length=100, verbose_name=u'name')
    value = models.CharField(max_length=100, verbose_name=u'value')

    __tablename__ = 'config'

    class Meta:
        db_table = 'config'
        verbose_name = verbose_name_plural = u'table'

    # def __str__(self):
    #     return self.name
