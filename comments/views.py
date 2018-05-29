from django.shortcuts import render, get_object_or_404, redirect
from onefirst.models import Post

from .forms import CommentForm
# Create your views here.


def post_comment(request, pk):
    # 获取被评论的文章
    post = get_object_or_404(Post, pk=pk)
    # 请求方式为post时处理表单请求
    if request.method == 'POST':

        # 用户提交的数据存在request.POST中，这是一个类字典对象
        # 利用提交的数据构造CommentForm实例，这个Django的表单就生成了。
        form = CommentForm(request.POST)

        # form.is_valid()方法，Django检查表单是否符合格式要求
        if form.is_valid():

            # 检查到数据合法，调用表单save方法保存表单到数据库
            # commit=Fales 的作用是仅仅利用表单的数据生成Comment模型类的实例，但还不进行保存
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来
            comment.post = post

            # 最终将评论数据保存进数据库，调用模型实例sava方法
            comment.save()

            # 重定向到post的详情页，实际上当redirect函数接受一个模型实例时，它它会调用这个模型实例的 get_absolute_url 方法
            # 然后重定向到get_absolute_url 方法返回的URL。
            return redirect(post)
        else:
            # 检查到数据不合格，重新渲染详情页，并且渲染表单的错误
            # Post 和 Comment 是Foreignkey 关联的
            # 所以post.comment_set.all()方法反向查询所有评论,获取改篇文章下所有评论
            # post.comment_set.all 等价与 Comment.objects.filter(post=post)
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render(request, 'onefirst/detail.html', context=context)
    return redirect(post)



