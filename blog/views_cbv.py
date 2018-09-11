#원래는 별도의 파일로 만드는게 맞음  blog/forms.py
from django import forms
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class ListView(ListView):   # 이렇게 해도되고 밑에처럼 해도 되고
    model = Post
    queryset = Post.objects.all().prefetch_related('tag_set')
    # paginate_by = 10

post_list = ListView.as_view()

                                    #cbv prefetch_related
# post_list = ListView.as_view(model=Post, queryset=Post.objects.all().prefetch_related('tag_set'), paginate_by=5)

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields= '__all__')

post_new = CreateView.as_view(model=Post, fields = '__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'

# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     # success_url = '/...'
