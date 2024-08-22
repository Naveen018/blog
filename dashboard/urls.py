from django.urls import include, path

from dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("categories/", views.categories, name="categories"),
    path("categories/add/", views.add_category, name="add_category"),
    path("categories/edit/<int:id>/", views.edit_category, name="edit_category"),
    path("categories/delete/<int:id>/", views.delete_category, name="delete_category"),
]
