from django.urls import include, path

from dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # category crud
    path("categories/", views.categories, name="categories"),
    path("categories/add/", views.add_category, name="add_category"),
    path("categories/edit/<int:id>/", views.edit_category, name="edit_category"),
    path("categories/delete/<int:id>/", views.delete_category, name="delete_category"),
    
    # blog post crud
    path("posts/", views.posts, name="posts"),
    path("posts/add/", views.add_post, name="add_post"),
    path("posts/edit/<int:id>/", views.edit_post, name="edit_post"),
    path("posts/delete/<int:id>/", views.delete_post, name="delete_post"),
]
