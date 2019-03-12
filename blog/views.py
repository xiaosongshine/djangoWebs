from django.shortcuts import render

from django.http import HttpResponse
from .models import *




#首页
def index(request):
    return render(request,'index.html')


#列表页
def lists(request,lid):
    pass

#内容页
def details(request):
    return render(request,'details.html')

#标签页
def tag(request, tag):
    pass

# 搜索页
def search(request):
    pass
# 关于我们
def about(request):
    pass
