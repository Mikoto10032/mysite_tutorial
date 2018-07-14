from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from article.models import Article
from datetime import datetime

# Create your views here.

'''
http://127.0.0.1:8000/
'''
def index(request):
    return HttpResponse('HelloWorld!')


def detail(request, my_args):
    return HttpResponse("You are looking at my_args %s."%my_args)


def detail2(request, my_args):
    post = Article.objects.all()[my_args] # 这不是一个错误,是因为IDE无法深入到该模块
    str = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)


def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})


def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})