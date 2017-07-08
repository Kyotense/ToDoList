# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.template import Context, Template
from todolist.models import Item
from django.views.generic import ListView
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
#@login_required(login_url="login/")
def index(request):
    return render(request, "todolist/index.html")

#@login_required(login_url="login/")
def add_item(request):
    if (request.method=="POST"):
        title = request.POST["title"]
        priority = request.POST["priority"]

        item = Item(title=title, priority=priority)

        item.save()

    return redirect("/")

def register(request):
    if (request.method=="POST"):
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        user.save()

    return redirect("/")


class Item_List(ListView):
    template_name = "todolist/list.html"
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.all()

#@login_required(login_url="login/")
def delete_items(request, item_pk):
    query = Item.objects.get(pk=item_pk)
    query.delete()
    return redirect("/")
