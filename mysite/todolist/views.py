# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.template import Context, Template
from todolist.models import Item, User
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required(login_url="login/")
def index(request):
    return render(request, "todolist/index.html")

@login_required(login_url="login/")
def add_item(request):
    if (request.method=="POST"):
        title = request.POST["title"]
        priority = request.POST["priority"]

        item = Item(title=title, priority=priority)

        item.save()

    return redirect("/")

def register(request):
    pass


class Item_List(LoginRequiredMixin, ListView):
    template_name = "todolist/list.html"
    context_object_name = "items"

    def get_queryset(self):
        return Item.objects.all()
