from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='home'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #re_path('<int:pk>/', views.post_detail, name='post_detail'),
    #re_path(r'^(?P<slug>\w+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),

    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    # re_path('<slug:slug>/', views.post_detail, name='post_detail')


]
