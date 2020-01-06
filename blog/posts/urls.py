from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name="list"),
    url(r'^create/$', views.create_post, name="create_post"),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/update/$', views.post_update, name='post_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.category_post, name="category_post"),
    # url(r'^(?P<slug>[\w-]+)/comment/$', views.add_comment_to_post, name="add_comment_to_post"),
    url(r'^comment/(?P<id>[\w-]+)/delete/$', views.comment_delete, name="comment_delete"),
]
