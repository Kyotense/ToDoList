from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView

urlpatterns = [
    url(r'^$', index.as_view()),
    url(r'^list/(?P<pk>\d+)$', DetailView.as_view(model = Item,
                                    template_name= 'todolist/list.html')),
]
