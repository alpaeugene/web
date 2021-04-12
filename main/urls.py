from django.urls import path
from . import views
from .views import PostWeb
from .views import CreatePostView

urlpatterns = [

    path('', views.prev, name='main'),
    #path('about', CreatePostView.as_view(), name='about-cat'),
    path('create', views.create, name='create'),
    #path('t1', views.t1, name='t1'),
    #path('t1', PostWeb.as_view(), name='t1'),
    path('last-news', views.news, name='last-news'),
    path('otziv', views.comment, name='otziv'),
    path('cat-info', views.bio, name='cat-info'),
    path('create-otziv', views.sc, name='create-otziv'),
    path('inf', views.inf, name='inf'),
    #path('prev', views.prev, name='prev'),
    path('lastn', views.lastn, name='lastn'),
    path('com', views.com, name='com'),
    #path('main1', views.main, name='main1'),
]
