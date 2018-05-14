from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible



@python_2_unicode_compatible
class Category(models.Model):
    """文章分类表"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    """文章标签"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """

    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文，我们使用了 TextField。
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    # 指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    author = models.ForeignKey(User)

    def __str__(self):
        return self.excerpt

    def get_absolute_url(self):
        return reverse('onefirst:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']