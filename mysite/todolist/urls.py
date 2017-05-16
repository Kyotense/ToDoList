from django.conf.urls import url, include
from . import views
from todolist.views import index
from todolist.models import Item, List
from django.views.generic import ListView, DetailView

urlpatterns = [
    #url(r'^$', views.main, name='main'),
    url(r'^$', index.as_view()),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Item,
                                    template_name= 'todolist/list.html')),
]
