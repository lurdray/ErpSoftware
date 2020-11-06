from django.urls import path
from . import views

app_name = "project"

urlpatterns = [

	path("add-project/", views.AddProjectView, name="add_project"),

	path("project-detail/<int:project_id>/", views.ProjectDetailView, name="project_detail"),

	path("project-comment/<int:project_id>/", views.CommentView, name="project_comment"),
	path("project-gallery/<int:project_id>/", views.GalleryView, name="project_gallery"),
	
	path("all-project/", views.AllProjectView, name="all_project"),
	path("delete-project/", views.DeleteProjectView, name="delete_project"),
	path("edit-project/", views.EditProjectView, name="edit_project"),
]
