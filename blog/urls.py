from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^$', views_cbv.post_list, name='post_list'), #중복의 우려가 있음
    url(r'^adadadadadad/(?P<pk>\d+)/$', views_cbv.post_detail, name='post_detail'),

    url(r'^comment/$', views.comment_list, name='comment_list'),

    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit$', views.post_edit, name='post_edit'),

    url(r'^cbv/new/$', views_cbv.post_new),
    url(r'^cbv/(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),
    url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete, name='post_delete'),
 ]
