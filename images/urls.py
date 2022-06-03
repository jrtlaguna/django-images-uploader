from django.urls import path

from images import views

app_name = "images"

urlpatterns = [
    path("", views.index, name="index"),
    path("active/", views.show_active, name="active"),
    path("archived/", views.show_archived, name="archived"),
    path("deleted/", views.show_deleted, name="deleted"),
    path("<int:image_id>/archive", views.archive_image, name="archive"),
    path("<int:image_id>/delete", views.delete_image, name="delete"),
]
