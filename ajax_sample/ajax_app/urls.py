from django.conf.urls import url
from ajax_app import views

urlpatterns = [
    url(r'^index/$',views.index,name = 'index'),
    url(r'^likepost/$',views.LikePost,name='likepost'),
]
