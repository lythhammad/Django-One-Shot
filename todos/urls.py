from django.urls import path
from todos.views import todo_list_view

urlpatterns = [
    path("", todo_list_view, name="show_list"),
]
