from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout
#from todolist.views import index, item_list
from todolist.views import Item_List
from todolist.models import Item
from django.contrib.auth import views as auth_views
#from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', Item_List.as_view()),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'registration/logout.html'}),
    url(r'^add', views.add_item, name="add"),
    #url(r'^list/$', Item_List.as_view()),
]
