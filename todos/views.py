from django.shortcuts import render
from todos.models import TodoList


def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/list.html", context)
