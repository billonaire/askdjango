from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib import messages

def post_list(request):  # comment_set 쓸때만쓰자
    qs = Post.objects.prefetch_related('tag_set').all()

    # 1/0  -> 500 Error

    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains=q)

    messages.error(request, '테스트')

    return render(request, 'blog/post_list.html',{
        'post_list':qs,
        'q' : q,
    }) #렌더할떄는 인자를 써줘야함

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, id=id)  #한 줄로 간편하게.

    return render(request, 'blog/post_detail.html',{
        'post': post,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # post.user = request.user  # 회원아니면 글못쓰게 하기
            # post.save()
            messages.success(request, '새 글이 등록되었습니다')
            return redirect(post)   # post.get_absolute_url()
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html',{
            'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            # post.user = request.user
            # post.save()
            messages.success(request, '새 글이 수정되었습니다')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html',{
            'form': form,
    })


def comment_list(request):
    comment_list = Comment.objects.all().select_related('post')
    return render(request, 'blog/comment_list.html',{
            'comment_list': comment_list,
    })
