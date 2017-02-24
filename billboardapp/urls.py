from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews


app_name = 'billboardapp'

urlpatterns = [
    # ex: /billboardapp/
    url(r'^$', views.index, name='index'),
    # ex: /billboardapp/addpost/
    url(r'^addpost$', views.addpost, name='addpost'),
    # ex: /billboardapp/delpost/
    url(r'^delpost$', views.deletePost, name='delpost'),
    url(R'^login/$', authviews.login, name='login'),
    url(R'^logout/$', authviews.logout, {'next_page': '/billboardapp'}, name='logout'),
]