from django.shortcuts import render, redirect, get_object_or_404
from todos.models import TodoList, TodoListForm


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


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect("todo_list_detail", id=todo_list.id)
    else:
        form = TodoListForm()
    context = {"form": form}
    return render(request, "todos/creat.html", context)
