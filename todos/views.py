from django.shortcuts import render, get_object_or_404
from todos.models import TodoList


def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    task_list = get_object_or_404(TodoList, id=id)
    context = {
        "task_list": task_list,
    }
    return render(request, "todos/detail.html", context)
