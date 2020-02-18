"""CBV_sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from cbv_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('create',views.cbv_create.as_view()),
    path('detail/<pk>',views.cbv_detail.as_view(),name='detail'),
    path('delete/<pk>',views.cbv_delete.as_view(),name ='delete'),
    path('update/<pk>',views.cbv_update.as_view(),name='update'),
    path('myform',views.cbv_my_form.as_view(),name='myform'),
    url('',views.cbv_list.as_view(),name='detail'),

]
