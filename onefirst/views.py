from django.shortcuts import render, get_object_or_404

from comments.forms import CommentForm
from onefirst.models import Post, Category
import markdown


# 主页
def index(request):
    post_list = Post.objects.all()
    return render(request, 'onefirst/index.html', context={'post_list': post_list})


# 文章详情页
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    # 获取这篇post下的全部评论
    comment_list = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板传递给detail.html模板，以便渲染相应数据
    context = {'post': post,
               'form': form,
               'comment_list': comment_list}
    return render(request, 'onefirst/detail.html', context=context)


# 文章归档
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    )
    return render(request, 'onefirst/index.html', context={'post_list': post_list})


# 文章分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'onefirst/index.html', context={'post_list': post_list})