from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews
from .views import PostList

app_name = 'billboardapp'

urlpatterns = [
    # ex: /billboardapp/
    url(r'^$', views.index, name='index'),
    
    # ex: /billboardapp/addpost/ &  # ex: /billboardapp/addcomment/
    url(r'^addpost$', views.addpost, name='addpost'),
    url(r'^addcomment', views.addcomment, name='addcomment'),
    
    # ex: /billboardapp/delpost/
    url(r'^delpost$', views.deletePost, name='delpost'),
    url(r'^delcomment$', views.deleteComment, name='delcomment'),

    url(R'^login/$', authviews.login, name='login'),
    url(R'^logout/$', authviews.logout, {'next_page': '/billboardapp'}, name='logout'),
    
    # register new user
    url(r'^registeruserpage/$', views.registerUserPage, name='register'),
    url(r'^registeruser/$', views.addUser, name='registerUser'),

    # test to add random list
    url(r'^postlist/$', views.PostList.as_view()),
]