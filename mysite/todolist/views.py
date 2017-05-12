from django.shortcuts import render, render_to_response
from django.template import Context, Template
from todolist.models import List, Item
from django.views.generic import ListView


def index(request):
    return render(request, 'todolist/todo.html')

def list_index(request):
    template_name = 'todolist/list_index.html'
    context_object_name = "lists"
    queryset = List.objects.all().order_by("title")

def add_list(request):
    pass

def add_item(request):
    if(request.method == "POST"):
        title = request.POST['title']
        priority = request.POST['priority']
        todo_list = request.POST['todo_list']

        item = Item(title=title, priority=priority, todo_list=todo_list)

        


def list_index(request):
    pass
