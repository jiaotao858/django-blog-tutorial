from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField('用户名', max_length=100)
    email = models.EmailField('Email', max_length=255)
    url = models.URLField('URL', blank=True)
    text = models.TextField('评论信息')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    post = models.ForeignKey('onefirst.Post', verbose_name='评论文章')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = '评论列表'
        verbose_name_plural = '评论列表'