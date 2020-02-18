"""CRUD_FBV URL Configuration

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
from FBV_app import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'<id>/delete',views.delete_view),
    path(r'<id>/detail',views.detail_view),
    path(r'<id>/update',views.update_view),
    path(r'create',views.create_view),
    path(r'',views.list_view),
    #max_id_now = 15
]
