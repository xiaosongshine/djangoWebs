from django.shortcuts import render

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *




#首页
def index(request):
    allarticle = Article.objects.all().order_by('-id')
    allcategory = Category.objects.all()#通过Category表查出所有分类
    hot = Article.objects.all().order_by('-views')[:6]#通过浏览数进行排序

    page = request.GET.get('page')#在URL中获取当前页面数
    paginator = Paginator(allarticle, 3)#对查询到的数据对象list进行分页，设置超过1条数据就分页
    try:
        allarticle = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        allarticle = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    return render(request,'index.html',locals())


#列表页
def lists(request,lid):
    allcategory = Category.objects.all()#通过Category表查出所有分类
    hot = Article.objects.all().order_by('-views')[:6]#通过浏览数进行排序
    #把查询出来的分类封装到上下文里
    context = {
            'allcategory': allcategory,
    }
    return render(request, 'list.html', locals())#把上下文传到index.html页面
#内容页
def details(request,did):
    show = Article.objects.get(id=did)#查询指定ID的文章
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'details.html', locals())

#标签页
def tag(request, tag):
    pass

# 搜索页
def search(request):
    cname = "查找结果"
    ss=request.GET.get('search')#获取搜索的关键词
    allarticle = Article.objects.filter(title__icontains=ss)#获取到搜索关键词通过标题进行匹配
    page = request.GET.get('page')
    allcategory = Category.objects.all()#通过Category表查出所有分类
    hot = Article.objects.all().order_by('-views')[:6]#通过浏览数进行排序
    paginator = Paginator(allarticle, 6)
    try:
        allarticle = paginator.page(page) # 获取当前页码的记录
    except PageNotAnInteger:
        allarticle = paginator.page(1) # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages) # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'list.html', locals())
# 关于我们
def me(request):
    return render(request,'me.html')

def sort(request,sid):

    hot = Article.objects.all().order_by('-views')[:6]#通过浏览数进行排序

    allarticle = Article.objects.filter(category_id=sid)#获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=sid)#获取当前文章的栏目名
    allcategory = Category.objects.all()#通过Category表查出所有分类

    page = request.GET.get('page')#在URL中获取当前页面数
    paginator = Paginator(allarticle, 3)#对查询到的数据对象list进行分页，设置超过1条数据就分页

    try:
        allarticle = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        allarticle = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容


    return render(request, 'sort.html', locals())#把上下文传到index.html页面

def archive(request,tid):
    hot = Article.objects.all().order_by('-views')[:6]#通过浏览数进行排序
    allarticle = Article.objects.filter(tui_id=tid)
    allTag = Tui.objects.all()#通过Category表查出所有分类
    cname = Tui.objects.get(id=tid)#获取当前文章的栏目名

    page = request.GET.get('page')#在URL中获取当前页面数
    paginator = Paginator(allarticle, 3)#对查询到的数据对象list进行分页，设置超过1条数据就分页
    try:
        allarticle = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        allarticle = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容


    return render(request, 'archive.html', locals())#把上下文传到index.html页面
