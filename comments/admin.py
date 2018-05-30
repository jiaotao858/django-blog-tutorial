from django.contrib import admin
from comments.models import Comment
# 后台管理模块


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['name', 'email', 'url', 'text',  'created_time', 'post']

    # 设置每页显示多少条记录，默认是100
    list_per_page = 30

    # 设置可以编辑字段
    # list_editable = ['title', 'category', 'author']

    # 设置显示外键字段
    # fk_fields =[]

    # 列表包含根据指定字段搜索
    search_fields = ('name', 'email', 'url', 'text')

    # 右侧过滤选项
    list_filter = ('name', )

    # 详细时间分层查询
    date_hierarchy = 'created_time'

    # 字段集合分组设置
    # fieldsets = (
    #     ('基本信息', {'fields': ('title',)}),
    #     ('Meta Data', {'fields': ('excerpt', 'category')}),
    # )

    # ManyToMany多对多字段设置
    # filter_horizontal = ('tags',)

    # 只显示相关字段
    # fields = ('title',)
    # exclude = ('title',)

    # 设置字段只读
    # def get_readonly_fields(self, request, obj=None):
    #     """  重新定义此函数，限制普通用户所能修改的字段  """
    #     if request.user.is_superuser:
    #         self.readonly_fields = []
    #     return self.readonly_fields

    readonly_fields = ('post',)
