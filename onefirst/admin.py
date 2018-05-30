from django.contrib import admin
from onefirst.models import Category, Tag, Post, Contact, User
# 后台管理模块

# 调整页面头部显示内容和页面标题
admin.site.site_header = '博客管理系统'
admin.site.site_title = 'VIP'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['title', 'excerpt', 'category', 'author',  'created_time', 'views']

    # 设置每页显示多少条记录，默认是100
    list_per_page = 30

    # 设置可以编辑字段
    # list_editable = ['title', 'category', 'author']

    # 设置显示外键字段
    # fk_fields =[]

    # 列表包含根据指定字段搜索
    search_fields = ('title', 'body')

    # 右侧过滤选项
    list_filter = ('author', )

    # 详细时间分层查询
    date_hierarchy = 'created_time'

    # 字段集合分组设置
    # fieldsets = (
    #     ('基本信息', {'fields': ('title',)}),
    #     ('Meta Data', {'fields': ('excerpt', 'category')}),
    # )

    # ManyToMany多对多字段设置
    filter_horizontal = ('tags',)

    # 只显示相关字段
    # fields = ('title',)
    # exclude = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['name', 'subject', 'message', 'email', 'create_time']

    # 设置每页显示多少条记录，默认是100
    list_per_page = 30


# 用户名密码
@admin.register(User)
class PostAdmin(admin.ModelAdmin):

    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['username', 'password']


# 注册模块
admin.site.register(Category)
admin.site.register(Tag)
