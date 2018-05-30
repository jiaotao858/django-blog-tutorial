from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
from django.utils.six import python_2_unicode_compatible
import markdown


# 登陆及注册模型
@python_2_unicode_compatible
class User(models.Model):
    username = models.CharField(max_length=21)
    password = models.CharField(max_length=21)


@python_2_unicode_compatible
class Category(models.Model):
    """文章分类表"""
    name = models.CharField('分类', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


@python_2_unicode_compatible
class Tag(models.Model):
    """文章标签表"""
    name = models.CharField('标签', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


@python_2_unicode_compatible
class Post(models.Model):
    """文章内容表"""

    # 文章标题
    title = models.CharField('标题', max_length=70)

    # 文章正文，我们使用了 TextField。
    body = models.TextField('正文')

    # 文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField('创建时间')
    modified_time = models.DateTimeField('修改时间')

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。一个文章只对应一个类型，一个类型可以对应多篇文章，一对多ForeignKey
    category = models.ForeignKey(Category, verbose_name='分类')
    # 一篇文章可以对应多个标签，一个标签也可以对应多个文章，多对都关系，多个多MonyToManyField
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    author = models.ForeignKey(User, verbose_name='作者')

    # 文章阅读量，PositiveIntegerField只可以为正和0，不可以为非负数
    views = models.PositiveIntegerField('阅读量', default=0)

    # __str__()方法为显示内容
    def __str__(self):
        return self.excerpt

    """
    函数get_absolute_url：获取文章据对路径
    1.视图函数命名空间app_name = 'onefirst'
    2.name=detail的视图
    3.reverse函数解析该视图的URL
    4.post/(?P<pk>[0-9]+)/中的正则部分被kwargs中pk替换掉
    5.最终该函数返回结果如/post/255/,这样Post 自己就生成了自己的 URL
    """
    def get_absolute_url(self):
        return reverse('onefirst:detail', kwargs={'pk': self.pk})

    # 页面自增，可以统计文章阅读量
    def increase_view(self):
        self.views += 1
        self.save(update_fields=['views'])

    # 读写save方法，使其支持自动截取功能
    def save(self, *args, **kwargs):
        # 如何没有填写摘要
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:199]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

    # 文章默认排列顺序
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-created_time']


@python_2_unicode_compatible
class Contact(models.Model):
    """联系我们表"""
    name = models.CharField('用户', max_length=100)
    email = models.EmailField('Email', max_length=255)
    subject = models.CharField('主题', max_length=100)
    message = models.TextField('内容', max_length=1000)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.message[:30]

    class Meta:
        verbose_name = '用户意见'
        verbose_name_plural = '用户意见'






