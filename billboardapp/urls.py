from django.conf.urls import url
from . import views


app_name = 'billboardapp'

urlpatterns = [
    # ex: /billboardapp/
    url(r'^$', views.index, name='index'),
    # ex: /billboardapp/addpost/
    url(r'^addpost$', views.addpost, name='addpost'),
    # ex: /billboardapp/delpost/
    url(r'^delpost$', views.deletePost, name='delpost'),
]