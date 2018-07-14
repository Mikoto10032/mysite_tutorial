"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path
from learn import views as learn_views  # learn
from article import views as article_views  # article

urlpatterns = [
    # path('', learn_views.index),    # learn
    path('', article_views.home),  # article的主页
    path('admin/', admin.site.urls),    #article的管理员界面
    # path('<my_args>', article_views.detail, name='detail')
    path('<int:my_args>', article_views.detail2, name='detail2'),
    path('test/', article_views.test),
]
