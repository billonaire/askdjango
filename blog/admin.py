from django.contrib import admin
from .models import Post, Comment, Tag


# 이렇게 쓰나 저렇게 쓰나 같음
# admin.site.register(Post, PostAdmin)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','tag_list','status','content', 'content_size','created_at', 'updated_at',]
    actions = ['make_published']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    def tag_list(request, post):
        return ','.join(tag.name for tag in post.tag_set.all())

    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} sucessfully marked as published'.format(updated_count))
    make_published.short_description = 'Mark selected stories as published'


# admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'message', 'post_content_len']
    # list_select_related = ['post'] 이거 써도 되고 밑에꺼 써도됨

    def post_content_len(self, comment):
        return '{}글자'.format(len(comment.post.content))

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('post')




@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
