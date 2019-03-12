"""XSsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib import admin
from blog.views import *

from django.urls import path, include, re_path
#上面这行多加了一个re_path
from django.views.static import serve
#导入静态文件模块
from django.conf import settings
#导入配置文件里的文件上传配置


urlpatterns = [
    path("",index),
    path('list-<int:lid>.html', lists, name='lists'),#列表页
    #path('details-<int:sid>.html', details, name='details'),#内容页
    path('details/', details, name='details'),#内容页
    path('tag/<tag>', tag, name='tags'),#标签列表页
    path('search/', search, name='search'),#搜索列表页
    path('about/', about, name='about'),#联系我们单页
    path("admin/", admin.site.urls),
    path("ueditor/", include("DjangoUeditor.urls")),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),#增加此行

]