from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.recent_posts, name='recent_posts'),
    url(r'^post$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]