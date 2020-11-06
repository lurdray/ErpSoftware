from django.urls import path
from . import views

app_name = "department"

urlpatterns = [
	
	#customer service shit
	path("client-brief/", views.ClientBriefView, name="client_brief"),
	path("brief-detail/<int:brief_id>/", views.BriefDetailView, name="brief_detail"),


	path("overview/", views.IndexView, name="department_index"),
	path("tutorial/", views.TutorialView, name="department_tutorial"),
	path("profile/", views.ProfileView, name="department_profile"),
	path("setting/", views.SettingView, name="department_setting"),
	path("nofication/", views.NoficationView, name="department_nofication"),
	path("how-it-works/", views.HowItWorksView, name="department_how_it_works"),


	path("add-department/", views.AddDepartmentView, name="add_department"),
	path("all-department/", views.AllDepartmentView, name="all_department"),
	path("delete-department/", views.DeleteDepartmentView, name="delete_department"),
	path("edit-department/", views.EditDepartmentView, name="edit_department"),
	
]
