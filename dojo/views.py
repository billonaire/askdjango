import os
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.generic import DetailView


# def mysum(request, x, y=0, z=0):
    # return HttpResponse(int(x) + int(y) + int(z))
def mysum(request, numbers):
    # result = sum(map(int,numbers.split("/")))
    result = sum(map(lambda s: int(s or 0),numbers.split("/")))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('킹카님이 오셨군요^^. {}님. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '성운'
    return HttpResponse('''
        <h1>TaskCompany</h1>
        <p>{name}
        <p>시간을 드립니다
    '''.format(name=name))


def post_list2(request):
    return render(request, 'dojo/post_list2.html')


def post_list3(request):
    return JsonResponse({
    'message': '안녕, 파이썬&장고',
    'items': ['파이썬','장고','Celery','Azure','AWS'],
    }, json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    filepath = '/Users/성운/py/django/askdjango/asdf.xls'
    # filepath = os.path.join(settings.BASE_DIR, 'asdf.xls') 작동이안됨
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response


#한줄로 편리하게.
post_detail = DetailView.as_view(model=Post, pk_url_kwarg='id')



def post_new(request):
    if request.method == 'POST':      #GET방식에서는 로직을 처리할게 많이 없기떄문
        form = PostForm(request.POST, request.FILES)  #FILES가 있어야 업로드가능
        if form.is_valid():  #유효성

            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()             깐단하게.
            post = form.save(commit=False)   # --> forms.py
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') # namespace:name 을 쓰는것을 추천
    else:
        form = PostForm()
    return render(request, 'dojo/post_form.html',{
        'form':form,
    })



def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/') # namespace:name 을 쓰는것을 추천
    else:
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html',{
        'form':form,
    })
