from django.contrib import admin

from django.apps import apps, AppConfig
# Register your models here.

from dj2.settings import dbName as schemaName
from main.users_model import users
from main.config_model import config

try:
    from main.models import *
except:
    pass
# change title
admin.site.site_title = schemaName  # title
admin.site.site_header = schemaName  # header
admin.site.index_title = schemaName  # title

allModels = apps.get_app_config('main').get_models()

for ind, model in enumerate(allModels):

    class modelsite(admin.ModelAdmin):
        list_display = []
        for col in model._meta.fields:
            list_display.append(col.name)

        search_fields = list_display


    admin.site.register(model, modelsite)
