from django.conf.urls import url, include
from . import views
from todolist.views import index, item_list
from todolist.models import Item, List
from django.views.generic import ListView, DetailView

urlpatterns = [
    #url(r'^$', views.main, name='main'),
    url(r'^$', index.as_view()),
    url(r'^(?P<todo_list_id>\d+)$', item_list.as_view()),
]
