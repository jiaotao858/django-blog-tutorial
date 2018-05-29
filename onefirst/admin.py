from django.contrib import admin
from onefirst.models import Category, Tag, Post
# Register your models here.
# 后台管理模块


class PostAdmin(admin.ModelAdmin):
    """定制Admin视图"""
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


# 注册模块
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
