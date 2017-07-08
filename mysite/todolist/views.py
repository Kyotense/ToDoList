# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.template import Context, Template
from todolist.models import Item
from django.views.generic import ListView


# Create your views here.
def index(request):
    return render(request, "todolist/index.html")

def add_item(request):
    if (request.method=="POST"):
        title = request.POST["title"]
        priority = request.POST["priority"]

        item = Item(title=title, priority=priority)

        item.save()

    return redirect("/")


class Item_List(ListView):
    template_name = "todolist/list.html"
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.all()

def delete_items(request, item_pk):
    query = Item.objects.get(pk=item_pk)
    query.delete()
    return redirect("/")
