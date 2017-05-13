from django.shortcuts import render, render_to_response
from django.template import Context, Template
from todolist.models import List, Item
from django.views.generic import ListView


def index(request):
    template_name = 'todolist/todo.html'
    context_object_name = "lists"
    queryset = List.objects.all().order_by("title")

def add_list(request):
    if(request.method == "POST"):
        title = request.POST['title']

        lst = List(title=title)

        lst.save()

def add_item(request):
    if(request.method == "POST"):
        title = request.POST['title']
        priority = request.POST['priority']
        todo_list = request.POST['todo_list']

        item = Item(title=title, priority=priority, todo_list=todo_list)

        item.save()
