from django.shortcuts import render
from django.utils import timezone
from .models import Post  # 引入你定义的模型

def post_list(request):
    # 这行代码是核心：去数据库里拿所有发布过的帖子，并按发布时间排序
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    # 把拿到的数据 (posts) 塞进那个大括号里，传给 HTML
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})