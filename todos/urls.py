from django.urls import path
from todos.views import todo_list_view, todo_list_detail

urlpatterns = [
    path("", todo_list_view, name="show_list"),
    path("<int:id>/", todo_list_detail, name="show_detail"),
]
