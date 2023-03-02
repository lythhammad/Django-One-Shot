from django.urls import path
from todos.views import todo_list_view, todo_list_detail, todo_list_create

urlpatterns = [
    path("create/", todo_list_create, name="todo_list_create"),
    path("", todo_list_view, name="show_list"),
    path("<int:id>/", todo_list_detail, name="show_detail"),
]
