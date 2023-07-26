from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # post [list,detail] func
    path("", views.post_list, name="post_list"),
    path("<int:id>", views.post_detail, name="post_detail"),
    # post [list,detail] func
    path("create", views.post_create, name="post_create"),
    path("<int:id>/edit", views.post_edit, name="post_edit"),
    # post [list,detail] cbv
    path("cbv", views.PostList.as_view(), name="post_list_cbv"),
    path("cbv/<int:pk>", views.PostDetail.as_view(), name="post_detail_cbv"),
]
