# -*-coding:utf-8 -*-
from django.contrib import admin
from blog.models import *


#常用的一些属性
#fileds\exclude
#filesets
#list_display
#list_display_links
#list_editable
#list_filter
#inlines
#参考资料
#https://docs.djangoproject.com/en/2.0/ref/contrib/admin/
#扩展阅读：admindocs的使用
#https://docs.djangoproject.com/en/2.0/ref/contrib/admin/admindocs


class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js=(
            '/static/js/kindeditor-4.1.11/kindeditor-all-min.js',
            '/static/js/kindeditor-4.1.11/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.11/config.js',
        )

# Register your models here.

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)