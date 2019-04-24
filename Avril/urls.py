"""Avril URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path
from Star.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base),
    path('index/',index),
    re_path(r'^$',start),
    path('list/',list),
    re_path(r'view/(?P<id>\d{1,2})',view),
    path('register/',register),
    path('register_data/',register_data),
    path('start/',start),
    path('star_list/',star_list),
    path('picwall/',picwall),
    path('search/',search),
    path('valid_code/',valid_code),
    re_path('article_detail/(?P<id>\d+)',article_detail),
    path("show/",show)
]
