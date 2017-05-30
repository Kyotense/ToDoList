from django.shortcuts import render, render_to_response
from django.template import Context, Template
from todolist.models import List, Item
from django.views.generic import ListView

def main(request):
    return render(request, 'todolist/main.html')

class index(ListView):
    template_name = 'todolist/todo.html'
    context_object_name = "lists"
    queryset = List.objects.all().order_by("title")

class item_list(ListView):
    template_name = 'todolist/list.html'
    context_object_name = "items"
    #queryset = Item.objects.all()

    def get_queryset(self):
        return Item.objects.filter(todo_list_id=self.kwargs.get('todo_list_id')).order_by("-priority")

def add_list(request):
    if(request.method == "POST"):
        title = request.POST['title']

        lst = List(title=title)

        lst.save()

def add_item(request):
    if(request.method == "POST"):
        queryset = List.objects.all().order_by("title")
        title = request.POST['title']
        priority = request.POST['priority']
        todo_list = request.POST['todo_list']

        item = Item(title=title, priority=priority, todo_list=todo_list)

        item.save()

        return redirect("/")
    else:
        return render(request, 'todolist/add.html')
