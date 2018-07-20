"""askdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path  #쉬워짐^^
from django.conf.urls.static import static

#url에 아무것도 안쳐도 blog로 가게하기
# def root(request):
#     return redirect('blog:post_list')

urlpatterns = [
    # url(r'^$', root, name='root'),    람다로 아주 간편하게; redirect.cbv로 쓰는 법도 있음
    url(r'^$', lambda r: redirect('blog:post_list'), name='root'),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),  #네임스페이스  각각 blog: 해줘야하는불편
    url(r'^blog/', include(('blog.urls','blog'), namespace='blog')),
    url(r'^dojo/', include('dojo.urls')),
    url(r'^shop/', include('shop.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 위에 올리면 NameError
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
