from django.conf.urls import url, include
from . import views
from todolist.views import Item_List
from todolist.models import Item
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', Item_List.as_view()),
    url(r'^add', views.add_item, name="add"),
    url(r'^delete/(?P<item_pk>.*)$', views.delete_items, name="delete"),
]
