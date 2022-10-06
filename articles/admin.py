from django.contrib import admin
from .models import Article, Dictionary
# Register your models here
# 
# .

admin.site.register(Article)


class LugatAdmin(admin.ModelAdmin):
    list_display = ['inglizcha','ozbekcha']

admin.site.register(Dictionary, LugatAdmin)
