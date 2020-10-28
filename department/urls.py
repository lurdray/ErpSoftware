from django.urls import path
from . import views

app_name = "department"

urlpatterns = [
	
	#customer service shit
	path("client-brief/", views.ClientBriefView, name="client_brief"),
	path("brief-detail/<int:brief_id>/", views.BriefDetailView, name="brief_detail"),




	path("department-home/", views.IndexView, name="department_index"),
	path("add-department/", views.AddDepartmentView, name="add_department"),
	path("all-department/", views.AllDepartmentView, name="all_department"),
	path("delete-department/", views.DeleteDepartmentView, name="delete_department"),
	path("edit-department/", views.EditDepartmentView, name="edit_department"),
	
]
